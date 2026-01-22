from app.people import Customer, Cleaner
from .hall import CinemaHall
from .bar import CinemaBar

__all__ = ["CinemaHall", "CinemaBar"]

hall = CinemaHall(number=5)
movie_name = "Madagascar"
customers = [
    Customer(name="Bob", food="Coca-cola"),
    Customer(name="Alex", food="popcorn")
]
cleaning_staff = Cleaner(name="Anna")

print(hall.movie_session(
    movie_name=movie_name,
    customers=customers,
    cleaning_staff=cleaning_staff
))
