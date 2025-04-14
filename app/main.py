from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    cinema_bar = CinemaBar()
    customer_list = []

    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data["food"])
        cinema_bar.sell_product(customer=customer, product=customer.food)
        customer_list.append(customer)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie_name, customer_list)

    cleaner = Cleaner(cleaning_staff)
    cleaner.clean_hall(hall_number)
