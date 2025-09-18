class Cleaner:
    """Funcionário da limpeza do cinema."""
    def __init__(self, name: str = "Cleaner"):
        self.name = name

    def clean(self, hall) -> str:
        number = getattr(hall, "number", None)
        if number is not None:
            return f"Cleaner {self.name} is cleaning hall number {number}."
        hall_label = getattr(hall, "name", "hall")
        return f"Cleaner {self.name} is cleaning {hall_label}."
    
    def clean_hall(self, hall_number: int) -> None:
        # exatamente o texto que os testes verificam
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
