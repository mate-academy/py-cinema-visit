from cinema.bar import CinemaBar
from cinema.hall import CinemaHall

from people.customer import Customer
from people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    movie_name: str,
    cleaning_staff: str
) -> None:
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)

    customer_objects = []

    for customer_name, food in customers:
        customer = Customer(customer_name, food)
        customer_objects.append(customer)

        if food:
            CinemaBar.sell_product(food, customer)

    hall.movie_session(
        movie_name,
        customer_objects,
        cleaner
    )


def main() -> None:
    pass
