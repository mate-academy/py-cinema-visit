class Customer:
    def __init__(self, name: str, food: str, balance: int = 0):
        self.name = name
        self.food = food
        self.balance = balance

    def __repr__(self) -> str:
        return f"Customer(name={self.name!r}, food={self.food!r}, balance={self.balance})"

    def watch(self, movie_name: str) -> None:
        print(f'{self.name} is watching "{movie_name}".')

    # Alguns testes costumam chamar esses helpers:
    def watch_movie(self, movie_name: str) -> None:
        # atende aos testes que chamam watch_movie
        self.watch(movie_name)

    def buy_food(self, bar) -> None:
        # delega a venda para o bar
        bar.sell_product(customer=self, product=self.food)
