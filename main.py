from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:

    customer_instances = [
        Customer(c["name"], c["food"]) for c in customers
    ]

    for person in customer_instances:
        CinemaBar.sell_product(person.food, person)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    hall.movie_session(movie, customer_instances, cleaning_staff)
