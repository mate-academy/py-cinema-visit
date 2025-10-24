class Customer:
    """
    Descreve um cliente do cinema, armazenando seu nome e o item de comida
    ou bebida que deseja comprar no bar.
    """
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        """
        Imprime o filme que o cliente está assistindo.
        """
        print(f"{self.name} is watching \"{movie}\".")
