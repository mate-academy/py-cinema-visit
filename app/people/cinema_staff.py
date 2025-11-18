class Cleaner:
    """
    Minimal Cleaner used by tests.
    """
    def __init__(self, name: str) -> None:
        self.name = name

    def clean(self, hall) -> None:
        hall.occupied = 0
