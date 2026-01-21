class Cleaner:
    """Class that represents cleaner in cinema"""
    def __init__(self, name: str) -> None:
        self.name = name

    # Method that prints message about cleaning hall
    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
