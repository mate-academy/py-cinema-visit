class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch(self, movie: str) -> str:
        return f"{self.name} is watching {movie}"
