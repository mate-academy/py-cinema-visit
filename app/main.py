from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    persons = []
    for customer in customers:
        person = Customer(customer["name"], customer["food"])
        persons.append(person)
        cinema_bar = CinemaBar()
        cinema_bar.sell_product(customer["food"], person)
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, persons, cleaner)
