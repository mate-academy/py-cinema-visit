from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_lst = []

    for customer in customers:
        customer_lst.append(
            Customer(name=customer["name"], food=customer["food"])
        )
        CinemaBar.sell_product(
            product=customer["food"],
            customer=Customer(name=customer["name"], food=customer["food"])
        )

    CinemaHall(number=hall_number).movie_session(
        movie_name=movie,
        customers=customer_lst,
        cleaning_staff=Cleaner(cleaner)
    )
