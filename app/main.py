# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner_name: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    cleaner = Cleaner(name=cleaner_name)

    customer_instances = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    cinema_hall = CinemaHall(number=hall_number)

    for customer in customer_instances:
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customer_instances, cleaner)
