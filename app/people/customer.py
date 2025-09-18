from app.cinema.bar import CinemaBar


class Customer:
    """Representa um cliente do cinema."""

    def __init__(self, name: str, balance: int = 0, food: str | None = None) -> None:
        self.name: str = name
        self.balance: int = balance
        self.food: str | None = food  # item de comida comprado (opcional)

    def watch_movie(self, movie_name: str) -> None:
        """Exibe que o cliente está assistindo ao filme."""
        print(f'{self.name} is watching "{movie_name}".')

    def buy_in_bar(self, cinema_bar: CinemaBar, product: str) -> None:
        """Cliente compra um produto no bar do cinema."""
        if self.food is None:
            cinema_bar.sell_product(self, product)
            self.food = product
