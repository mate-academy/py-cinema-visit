from app.people.customer import Customer


class Cleaner:
    def __init__(self, name: Customer) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
