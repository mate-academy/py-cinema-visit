# app/people/cinema_staff.py

class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    # O spec/CI pedem apenas imprimir, sem retornar nada
    def clean_hall(self, hall_number: int) -> None:
        print(f'{self.name} is cleaning hall {hall_number}')
