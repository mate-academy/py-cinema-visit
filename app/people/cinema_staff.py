class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean(self, hall_number: int) -> str:
        return f"{self.name} is cleaning hall {hall_number}"
