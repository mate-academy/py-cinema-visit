from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner_name: str,
        movie_name: str
) -> None:
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner_name)

    customer_instances = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]

    for customer in customer_instances:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    cinema_hall.movie_session(movie_name, customer_instances, cleaner)
