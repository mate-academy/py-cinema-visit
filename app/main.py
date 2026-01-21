from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customer_list = []
    for customer in customers:
        visitor = Customer(name=customer["name"], food=customer["food"])
        customer_list.append(visitor)
        CinemaBar.sell_product(visitor.food, visitor)
    CinemaHall(hall_number).movie_session(
        movie,
        customer_list,
        Cleaner(cleaner)
    )
