
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie_name: str) -> None:
        print(f"{self.name} is watching movie {movie_name}")