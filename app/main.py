from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict[str, str]], hall_number: int,
                 cleaner: str, movie: str) -> None:
    # creation of customers and their`s shopping
    customers_instances = []
    for customer in customers:
        customer_creation = Customer(customer["name"], customer["food"])
        customers_instances.append(customer_creation)
        CinemaBar.sell_product(customer_creation, customer_creation.food)

    cinema_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customers_instances, cinema_staff)
