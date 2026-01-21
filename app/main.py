from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers_data: list[dict],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    customers: list[Customer] = [
        Customer(data["name"], data["food"]) for data in customers_data
    ]

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)

    for customer in customers:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie_name, customers, cleaner)
