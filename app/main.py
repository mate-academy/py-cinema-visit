from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_objects: list[Customer] = []

    for data in customers:
        customer_obj = Customer(name=data["name"], food=data["food"])
        customer_objects.append(customer_obj)
        CinemaBar.sell_product(product=data["food"], customer=customer_obj)

    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj,
    )
