from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    for visiter in [Customer(
                    name=customer["name"],
                    food=customer["food"])
                    for customer in customers]:
        CinemaBar().sell_product(customer=visiter, product=visiter.food)
    CinemaHall(hall_number).movie_session(movie, customers, Cleaner(cleaner))
