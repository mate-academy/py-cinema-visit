from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customers_obj = []
    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=customer["food"])
        customers_obj.append(customer_obj)
        CinemaBar.sell_product(
            customer=customer_obj,
            product=customer_obj.food
        )

    CinemaHall(number=hall_number).movie_session(
        movie_name=movie,
        customers=customers_obj,
        cleaning_staff=Cleaner(name=cleaner)
    )
