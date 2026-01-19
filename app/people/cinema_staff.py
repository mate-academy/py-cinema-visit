class Cleaner:
    def __init__(self, name):
        self.name = name
    
    def clean_hall(self, hall_number: int) -> str:
        print(f"Cleaner {self.name} is cleaning hall {hall_number}.")