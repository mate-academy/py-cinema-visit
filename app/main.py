from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:

    customer_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customer_list:
        CinemaBar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customer_list, Cleaner(cleaner))
