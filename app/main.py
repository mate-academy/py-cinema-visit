from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_list = []
    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data["food"])
        customer_list.append(customer)
        CinemaBar.sell_product(customer_data["food"], customer)
    hall = CinemaHall(hall_number)
    stuff = Cleaner(cleaner)
    hall.movie_session(movie, customer_list, stuff)
