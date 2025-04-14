from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []
    hall = CinemaHall(hall_number)
    bar = CinemaBar()
    clean = Cleaner(cleaner)
    for person in customers:
        person = Customer(name=person["name"], food=person["food"])
        customers_list.append(person)
        bar.sell_product(person.food, person)
    hall.movie_session(
        movie,
        customers_list,
        clean,
    )
