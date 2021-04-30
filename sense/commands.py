import simpleaudio as sa
from typing import Dict


class TagCommand:
    """
    Command for triggering an action if a certain tag is present in the predictions.
    """
    def __init__(self, tag: str):
        self.tag = tag

    def __call__(self, predictions: Dict[str, any]):
        if predictions.get(self.tag):
            self.action()
        return True

    def action(self):
        raise NotImplementedError


class DrumCommand(TagCommand):
    def __init__(self, tag: str, wav_file_path: str):
        super().__init__(tag)
        self.sound = sa.WaveObject.from_wave_file(wav_file_path)

    def action(self):
        self.sound.play()
