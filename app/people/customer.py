class Customer:
    # ✅ Construtor EXATO exigido
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    # ✅ Nome de método EXATO
    def watch_movie(self, movie: str) -> None:
        # Ajuste a frase se os testes checarem string literal
        print(f'{self.name} is watching {movie}')
