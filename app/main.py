from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str,
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)

    customer_instances = []
    for cust in customers:
        customer = Customer(cust["name"], cust["food"])
        customer_instances.append(customer)
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie_name, customer_instances, cleaner)
