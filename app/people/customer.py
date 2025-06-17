class Customer:
    # Classe para um cliente do cinema
    def __init__(self, name: str, food: str) -> None:
        # Guarda nome e comida do cliente
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        # Imprime que o cliente está assistindo ao filme
        print(f'{self.name} is watching "{movie}".')
