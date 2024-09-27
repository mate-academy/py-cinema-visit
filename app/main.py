from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = []

    for customer in customers:
        person = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(person.food, person)
        customer_instances.append(person)

    cleaner = Cleaner(cleaner)
    CinemaHall(hall_number).movie_session(movie, customer_instances, cleaner)
