from app.main import cinema_visit
from app.cinema_bar import CinemaBar
from app.cinema_hall import CinemaHall
from app.cleaner import Cleaner

def test_cinema_visit():
    customers = ["Bob"]
    movie = "Tenet"
    menu = ["Popcorn"]
    cinema_bar = CinemaBar(name="Main Bar", location="Cinema Hall 1")
    cinema_hall = CinemaHall(1, 100)
    cleaner = Cleaner("Anna")

    cinema_visit(customers, movie, menu, cinema_bar, cinema_hall, cleaner)