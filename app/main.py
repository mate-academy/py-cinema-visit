from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    customer_instances = [
        Customer(person["name"], person["food"]) for person in customers
    ]

    for customer in customer_instances:
        cinema_bar.sell_product(customer.food, customer)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
