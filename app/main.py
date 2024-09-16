from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    customers = [Customer(customer.get("name"), customer.get("food"))
                 for customer in customers
                 ]

    cinema_hall_instance = CinemaHall(hall_number)

    cleaner_instance = Cleaner(cleaning_staff)
    cinema_bar_instance = CinemaBar()

    [cinema_bar_instance.sell_product(
        customer.food,
        customer
    )
        for customer in customers]
    cinema_hall_instance.movie_session(
        movie_name,
        customers,
        cleaner_instance
    )
