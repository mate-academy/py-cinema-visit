class Cleaner:
    """
    Descreve o membro da equipe responsável pela limpeza do cinema.
    """
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """
        Imprime que o faxineiro está limpando o corredor especificado.
        """
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
