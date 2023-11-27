from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
):

    customers = [
        Customer(customer["name"],
                 customer["food"])
        for customer in customers
    ]

    cinema_bar = CinemaBar()
    hall_number = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)

    for customer in customers:
        cinema_bar.sell_product(customer.food, customer)

    hall_number.movie_session(
        movie_name,
        customers,
        cleaner
    )
