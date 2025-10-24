class Cleaner:
    """
    Descreve um membro da equipe de limpeza do cinema.
    """
    def __init__(self, name: str):
        """
        Inicializa o limpador com um nome.
        name é o nome do limpador.
        """
        self.name = name

    def clean_hall(self, hall_number: int):
        """
        Imprime que o limpador está limpando uma sala específica.
        hall_number é o número da sala a ser limpa.
        """
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
