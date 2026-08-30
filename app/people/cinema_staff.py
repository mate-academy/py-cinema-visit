class Cleaner:
    def __init__(self, name):
        self.name = name

    def clean_hall(self, hall_number: int):
        self.hall_number = hall_number
        print(f"Cleaner {self.name} is cleaning hall number "
              f"{self.hall_number}.")
