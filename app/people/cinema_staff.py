class Cleaner:

    def __init__(self, name):
        self.name = name

    def clean_hall(self, hall_number):
        return print(f"Cleaner {self.name} is cleaning "
                     f"hall number {hall_number}.")
