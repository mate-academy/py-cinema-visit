class Cleaner:

    def __init__(self,name: str) -> None:
        self.name = name


    def clean_hall(self, hall_number: int):
        print(f"Cleaner is {self.name} cleaning hall number {hall_number}")

