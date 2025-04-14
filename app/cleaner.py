class Cleaner:
    def __init__(self, name):
        self.name = name

    def clean_hall(self, hall_id):
        print(f"Cleaner {self.name} is cleaning hall number {hall_id}.")