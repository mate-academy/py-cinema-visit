from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_objs = []

    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(
            product=customer_obj.food,
            customer=customer_obj
        )
        customer_objs.append(customer_obj)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaner_obj
    )
