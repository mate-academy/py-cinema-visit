from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:

    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)

    cinema_customers = []

    for customer_profile in customers:
        customer = Customer(customer_profile["name"], customer_profile["food"])
        cinema_customers.append(customer)
        cinema_bar.sell_product(customer.food, customer)

    hall.movie_session(movie_name, cinema_customers, cleaner)
