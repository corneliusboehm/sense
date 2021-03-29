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
import os

import sense.display
from sense import RESOURCES_DIR
from sense.commands import DrumCommand
from sense.controller import Controller
from sense.downstream_tasks.airdrums import INT2LAB
from sense.downstream_tasks.airdrums import LAB2INT
from sense.downstream_tasks.nn_utils import LogisticRegression
from sense.downstream_tasks.nn_utils import Pipe
from sense.downstream_tasks.postprocess import DetectEvent
from sense.downstream_tasks.postprocess import PostprocessClassificationOutput
from sense.loading import build_backbone_network
from sense.loading import get_relevant_weights
from sense.loading import ModelConfig
from sense.loading import update_backbone_weights


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

    # Load weights
    backbone_weights = weights['backbone']
    airdrums_checkpoint = weights['airdrums']

    # Update original weights in case some intermediate layers have been finetuned
    update_backbone_weights(backbone_weights, airdrums_checkpoint)
    backbone_network = build_backbone_network(selected_config, backbone_weights)

    # Load a logistic regression classifier
    airdrums = LogisticRegression(num_in=backbone_network.feature_dim,
                                  num_out=len(LAB2INT))
    airdrums.load_state_dict(airdrums_checkpoint)
    airdrums.eval()

    # Concatenate backbone network and rep counter
    net = Pipe(backbone_network, airdrums)

    postprocessor = [PostprocessClassificationOutput(INT2LAB, smoothing=4)]
    postprocessor.extend(
        DetectEvent(tag, idx, threshold=0.1) for tag, idx in LAB2INT.items()
    )

    display_ops = [
        sense.display.DisplayFPS(expected_camera_fps=net.fps,
                                 expected_inference_fps=net.fps / net.step_size),
        sense.display.DisplayTopKClassificationOutputs(top_k=3, threshold=0),
    ]
    display_results = sense.display.DisplayResults(title='AirDrums', display_ops=display_ops,
                                                   border_size=100)

    # Initialize Drum commands
    drum_commands = [
        DrumCommand("High Tom_position_1", os.path.join(RESOURCES_DIR, 'airdrums', 'Tom4.wav')),
        DrumCommand("Crash Cymbal_position_1", os.path.join(RESOURCES_DIR, 'airdrums', 'Ride4.wav')),
        DrumCommand("Hi-Hats_position_1", os.path.join(RESOURCES_DIR, 'airdrums', 'Hat5.wav')),
        DrumCommand("Ride Cymbal_position_1", os.path.join(RESOURCES_DIR, 'airdrums', 'Ride5.wav')),
        DrumCommand("Mid Tom_position_1", os.path.join(RESOURCES_DIR, 'airdrums', 'Tom5.wav')),
        DrumCommand("Floor Tom_position_1", os.path.join(RESOURCES_DIR, 'airdrums', 'Floor5.wav')),
        DrumCommand("Snare_position_1", os.path.join(RESOURCES_DIR, 'airdrums', 'Snare5.wav')),
        DrumCommand("Bass Drum_position_1", os.path.join(RESOURCES_DIR, 'airdrums', 'Kick5.wav')),
    ]

    # Run live inference
    controller = Controller(
        neural_network=net,
        post_processors=postprocessor,
        results_display=display_results,
        callbacks=drum_commands,
        camera_id=camera_id,
        path_in=path_in,
        path_out=path_out,
        use_gpu=use_gpu
    )
    controller.run_inference()
