class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} "
              f"is cleaning hall number {hall_number}.")


if __name__ == "__main__":
    anna = Cleaner(name="Anna")
    anna.clean_hall(hall_number=5)
