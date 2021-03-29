import numpy as np

from sense.display import BaseDisplay


class BaseAudioPlayer(BaseDisplay):
    """
    Base class for playing sounds depending on predictions.
    Sub-classes should overwrite the play method.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def display(self, img: np.ndarray, display_data: dict) -> np.ndarray:
        """
        Overwriting display from the BaseDisplay class.
        """
        self.play(display_data)
        return img

    def play(self, predictions: dict):
        """
        TODO
        """
        raise NotImplementedError


class PlaySoundOnEvent(BaseAudioPlayer):
    """
    TODO
    """

    def __init__(self, event: str, **kwargs):
        super().__init__(**kwargs)
        self.event = event

    def play(self, predictions: dict):
        """
        TODO
        """
        pass
