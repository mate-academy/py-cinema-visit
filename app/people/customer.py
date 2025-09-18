# app/people/customer.py

class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        # Saída EXATA exigida:
        # 'Bob is watching "Matrix".\n'
        print(f'{self.name} is watching "{movie}".')
