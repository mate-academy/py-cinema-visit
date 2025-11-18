class CinemaHall:
    """
    Minimal CinemaHall used by tests.
    """
    def __init__(self, capacity: int = 100) -> None:
        self.capacity = capacity
        self.occupied = 0

    def enter(self, count: int = 1) -> None:
        self.occupied += count

    def leave(self, count: int = 1) -> None:
        self.occupied = max(0, self.occupied - count)
