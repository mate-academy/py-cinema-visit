from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    customer_list = []

    for person in customers:
        customer_instance = Customer(person["name"], person["food"])
        CinemaBar.sell_product(person["food"], customer_instance)
        customer_list.append(customer_instance)

    cinema_hall.movie_session(movie, customer_list, cleaner_instance)
