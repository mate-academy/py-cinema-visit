class Customer:
    """
    Descreve um cliente do cinema, incluindo seu nome e a comida desejada.
    """
    def __init__(self, name: str, food: str):
        """
        Inicializa o cliente com nome e item de comida.

        name: O nome do cliente.
        food: O item de comida/bebida que o cliente deseja.
        """
        self.name = name
        self.food = food

    def watch_movie(self, movie: str):
        """
        Imprime o filme que o cliente está assistindo.

        movie: O nome do filme.
        """
        print(f"{self.name} is watching \"{movie}\".")

# Exemplo de uso
if __name__ == '__main__':
    bob = Customer(name="Bob", food="popcorn")
    bob.watch_movie(movie="Madagascar")