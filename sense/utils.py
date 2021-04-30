from typing import Dict
from typing import List


def clean_pipe_state_dict_key(key):
    to_replace = [
        ('feature_extractor', 'cnn'),
        ('feature_converter.', '')
    ]
    for pattern, replacement in to_replace:
        if key.startswith(pattern):
            key = key.replace(pattern, replacement)
    return key


class WriteToFileCallback:
    def __init__(self, labels: List[str], filename: str, lab2int: Dict[str, int]):
        self.labels = labels
        self.lab2int = lab2int

        self.file = open(filename, 'w')
        self.file.write(f'# {", ".join(self.labels)}\n')

    def __call__(self, predictions: Dict[str, any]):
        values = []
        prediction_dict = predictions["prediction"]
        if prediction_dict is None:
            return True

        for label in self.labels:
            values.extend([
                str(prediction_dict[self.lab2int[label]]),
                str(int(predictions[label]))
            ])
        self.file.write(', '.join(values) + "\n")
        return True
