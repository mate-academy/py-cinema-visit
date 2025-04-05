class Cleaner:
    def __init__(self, name):
        self.name = name

    def clean_hall(self, hall_number):
        # app/people/cinema_staff.py
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")