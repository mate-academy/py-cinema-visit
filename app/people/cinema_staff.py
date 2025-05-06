class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> str:
        return f"Cleaner {self.name} is cleaning hall number {hall_number}."

# anna = Cleaner(name="Anna")
# print(anna.clean_hall(hall_number=5))
# # Cleaner Anna is cleaning hall number 5.