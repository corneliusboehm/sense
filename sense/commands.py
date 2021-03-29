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

    def action(self):
        raise NotImplementedError
