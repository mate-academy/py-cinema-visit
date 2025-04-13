class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        result = f"Cleaner {self.name} is cleaning hall number {hall_number}."
        print(result)


if __name__ == "__main__":
    anna = Cleaner(name="Anna")
    anna.clean_hall(hall_number=5)
# Cleaner Anna is cleaning hall number 5.
    name = "Anatoly"
    cleaner = Cleaner(name=name)
    hall_number = 9
    cleaner.clean_hall(hall_number)
    "Cleaner Anatoly is cleaning hall number 9.\n"
