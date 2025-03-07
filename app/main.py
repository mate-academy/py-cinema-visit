from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    guests = []
    for human in customers:
        guests.append(Customer(human["name"], human["food"]))
    for human in guests:
        CinemaBar.sell_product(human, human.food)
    CinemaHall.movie_session(CinemaHall(hall_number),
                             movie,
                             guests,
                             Cleaner(cleaner))
