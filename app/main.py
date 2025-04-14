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
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    customer_instances = []

    for customer in customers:
        current_customer = (Customer(customer["name"], customer["food"]))
        customer_instances.append(current_customer)
        CinemaBar.sell_product(current_customer.food, current_customer)

    cinema_hall.movie_session(movie, customer_instances, cleaning_staff)
