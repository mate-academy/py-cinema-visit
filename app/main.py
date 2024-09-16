from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_instances = []
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for customer in customers:
        name = customer["name"]
        food = customer["food"]

        customer_model = Customer(name, food)
        cinema_bar.sell_product(customer_model, food)
        customers_instances.append(customer_model)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_instances,
        cleaning_staff=cleaner)
