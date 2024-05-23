from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:

    customer_instances = [
        Customer(name=cust["name"], food=cust["food"]) for cust in customers
    ]

    cinema_bar = CinemaBar()
    for customer in customer_instances:
        cinema_bar.sell_product(customer, customer.food)

    cleaner_instance = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
