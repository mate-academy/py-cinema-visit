from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = [
        Customer(person["name"], person["food"])
        for person in customers
    ]

    cinema_bar = CinemaBar
    staff = Cleaner(cleaner)

    for customer in customer_list:
        cinema_bar.sell_product(customer.food, customer)
    CinemaHall(hall_number).movie_session(movie, customer_list, staff)
