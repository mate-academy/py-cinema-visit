from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: str,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    all_customers = []

    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)

    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data["food"])
        cinema_bar.sell_product(customer, customer.food)
        all_customers.append(customer)

    hall.movie_session(movie_name, all_customers, cleaner)
