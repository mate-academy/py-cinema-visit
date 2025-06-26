from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customer_objs = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]
    for customer in customer_objs:
        CinemaBar.sell_product(
            customer=customer, product=customer.food
        )
    CinemaHall(hall_number).movie_session(
        movie, customer_objs, Cleaner(cleaner)
    )
