from cinema.bar import CinemaBar
from cinema.hall import CinemaHall
from people.customer import Customer
from people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    ch = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    for i in customers:
        CinemaBar.sell_product(i.name, i.food)
    ch.movie_session(movie, customers, clean.name)


cinema_visit([Customer("Bob", "kkk"), Customer("Mate", "ooo")], 5, "Nancy", "Graf")
