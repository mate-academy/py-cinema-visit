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
    customer_instance = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    cinemahall_instance = CinemaHall(hall_number)
    cinemabar_instance = CinemaBar()
    cleaner_instance = Cleaner(cleaner)

    for customer in customer_instance:
        cinemabar_instance.sell_product(customer, customer.food)

    cinemahall_instance.movie_session(
        movie, customer_instance, cleaner_instance
    )
