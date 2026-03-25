from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_list = []
    for customer in customers:
        customer_list.append(Customer(customer["name"], customer["food"]))
    cleaning_staff = Cleaner(cleaner)
    for customer in customer_list:
        CinemaBar.sell_product(customer.food, customer)
    CinemaHall(hall_number).movie_session(movie, customer_list, cleaning_staff)
