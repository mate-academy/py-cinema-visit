from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_obj = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for customer_obj in customers_obj:
        CinemaBar.sell_product(customer_obj, customer_obj.food)
    cleaner_obj = Cleaner(cleaner)
    cinema = CinemaHall(hall_number)
    cinema.movie_session(
        movie_name=movie,
        customers=customers_obj,
        cleaning_staff=cleaner_obj
    )
