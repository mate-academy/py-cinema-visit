class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def cleaning_hall(self, clean_hall: int) -> str:
        print(f"Cleaner {self.name} is cleaning hall number {clean_hall}.")
