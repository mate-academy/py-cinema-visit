"""
cinema_staff - inside this module create Cleaner class, its __init__ method
 takes and stores name. This class should have only one method clean_hall,
 this method takes hall_number - number of hall that cleaner have to clean
 and prints that cleaner is cleaning that hall.
anna = Cleaner(name="Anna")
anna.clean_hall(hall_number=5)
    # Cleaner Anna is cleaning hall number 5.
"""


class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
