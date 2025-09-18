class CinemaStaff:
    def __init__(self, name: str) -> None:
        self.name = name

    # ✅ Somente este método público; deve APENAS imprimir
    def clean_hall(self, hall_number: int) -> None:
        # Ajuste a frase se os testes checarem string literal
        print(f"{self.name} is cleaning hall {hall_number}")
