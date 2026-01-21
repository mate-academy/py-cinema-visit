class Cleaner:
    def __init__(self, name: str, hall_number: int = None) -> str:
        self.name = name
        self.hall_number = hall_number

    def clean_hall(self: str, hall_number: str) -> str:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")


if __name__ == "__main__":
    anna = Cleaner(name="Anna")
    anna.clean_hall(hall_number=5)
