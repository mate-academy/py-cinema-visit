from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    customers_list = []
    for guest in customers:
        customers_list.append(Customer(guest["name"], guest["food"]))

    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)
    CinemaHall(hall_number).movie_session(
        movie_name,
        customers_list,
        Cleaner(cleaning_staff)
    )
