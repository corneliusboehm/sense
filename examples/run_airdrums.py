#!/usr/bin/env python
"""
Play air drums in front of your webcam just using your hands.

Supported drums:
- Hi-Hats
- Snare
- High Tom
- Mid Tom
- Floor Tom
- Bass Drum (thump your chest)
- Crash Cymbal
- Ride Cymbal

Usage:
  run_airdrums.py [--camera_id=CAMERA_ID]
                  [--path_in=FILENAME]
                  [--path_out=FILENAME]
                  [--model_name=NAME]
                  [--model_version=VERSION]
                  [--use_gpu]
  run_airdrums.py (-h | --help)

Options:
  --camera_id=CAMERA_ID           ID of the camera to stream from
  --path_in=FILENAME              Video file to stream from
  --path_out=FILENAME             Video file to stream to
  --model_name=NAME               Name of the model to be used.
  --model_version=VERSION         Version of the model to be used.
  --use_gpu                       Whether to run inference on the GPU or not.
"""
from docopt import docopt

import sense.display
from sense.controller import Controller
from sense.downstream_tasks.airdrums import LAB2INT
from sense.downstream_tasks.nn_utils import LogisticRegression
from sense.downstream_tasks.nn_utils import Pipe
from sense.downstream_tasks.postprocess import DetectEvent
from sense.loading import build_backbone_network
from sense.loading import get_relevant_weights
from sense.loading import ModelConfig


SUPPORTED_MODEL_CONFIGURATIONS = [
    ModelConfig('StridedInflatedEfficientNet', 'pro', ['airdrums']),
]


if __name__ == "__main__":
    # Parse arguments
    args = docopt(__doc__)
    camera_id = int(args['--camera_id'] or 0)
    path_in = args['--path_in'] or None
    path_out = args['--path_out'] or None
    model_name = args['--model_name'] or None
    model_version = args['--model_version'] or None
    use_gpu = args['--use_gpu']

    # Load weights
    selected_config, weights = get_relevant_weights(
        SUPPORTED_MODEL_CONFIGURATIONS,
        model_name,
        model_version
    )

    # Load backbone network
    backbone_network = build_backbone_network(selected_config, weights['backbone'])

    # Load a logistic regression classifier
    airdrums = LogisticRegression(num_in=backbone_network.feature_dim,
                                  num_out=5)
    airdrums.load_state_dict(weights['airdrums'])
    airdrums.eval()

    # Concatenate backbone network and rep counter
    net = Pipe(backbone_network, airdrums)

    postprocessor = [
        DetectEvent(tag, idx) for tag, idx in LAB2INT.items()
    ]

    display_ops = [
        sense.display.DisplayFPS(expected_camera_fps=net.fps,
                                 expected_inference_fps=net.fps / net.step_size),
        sense.display.DisplayTopKClassificationOutputs(top_k=1, threshold=0.5),
    ]
    display_results = sense.display.DisplayResults(title='AirDrums', display_ops=display_ops,
                                                   border_size=100)

    # Run live inference
    controller = Controller(
        neural_network=net,
        post_processors=postprocessor,
        results_display=display_results,
        callbacks=[],
        camera_id=camera_id,
        path_in=path_in,
        path_out=path_out,
        use_gpu=use_gpu
    )
    controller.run_inference()
