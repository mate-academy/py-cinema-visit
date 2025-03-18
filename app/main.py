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
    hall_number = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customer_instances = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customer_instances.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    hall_number.movie_session(movie, customer_instances, cleaner)
    pass
