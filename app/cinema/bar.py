class CinemaBar:
    """
    Minimal CinemaBar used by tests.
    """
    def __init__(self) -> None:
        self.inventory: dict[str, float] = {}

    def add_item(self, name: str, price: float) -> None:
        self.inventory[name] = price

    def get_price(self, name: str) -> float | None:
        return self.inventory.get(name)
