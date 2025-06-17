class Cleaner:
    # Classe para o faxineiro do cinema
    def __init__(self, name: str) -> None:
        # Guarda o nome do faxineiro
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        # Imprime que o faxineiro está limpando a sala
        print(f'Cleaner {self.name} is cleaning hall number {hall_number}.')
