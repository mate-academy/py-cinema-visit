from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_visitors = []
    cleaner_instance = Cleaner(cleaner)

    for visitor in customers:
        customer_instance = Customer(visitor.get("name"), visitor.get("food"))
        CinemaBar.sell_product(
            customer=customer_instance,
            product=visitor.get("food")
        )

        cinema_visitors.append(customer_instance)

    cinema_instance = CinemaHall(number)
    cinema_instance.movie_session(movie, cinema_visitors, cleaner_instance)
