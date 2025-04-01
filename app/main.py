from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:

    customer_list = []
    for customer in customers:
        customer_class = Customer(customer["name"], customer["food"])
        customer_list.append(customer_class)
        CinemaBar.sell_product(
            customer=customer_class,
            product=customer["food"]
        )

    clean = Cleaner(name=cleaner)
    cinema = CinemaHall(number=hall_number)
    cinema.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=clean,
    )
