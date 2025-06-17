from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict[str, str]],
                 hall_number: int,
                 cleaner: str, movie: str) -> None:

    cinema: "CinemaHall" = CinemaHall(hall_number)

    customer_list: list["Customer"] = []

    for customer in customers:
        cb = CinemaBar()

        custom_object = Customer(customer["name"], customer["food"])

        cb.sell_product(custom_object, custom_object.food)

        customer_list.append(custom_object)

    cinema.movie_session(movie_name=movie,
                         customers=customer_list,
                         cleaning_staff=Cleaner(cleaner))
