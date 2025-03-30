from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    new_bar = CinemaBar
    for customer in customers:
        new_customer = Customer(customer.get("name"), customer.get("food"))
        new_bar.sell_product(new_customer.food, new_customer)
    new_session = CinemaHall(hall_number)
    customers = [
        Customer(customer.get("name"),
                 customer.get("food"))
        for customer in customers
    ]
    cleaner = Cleaner(cleaner)
    new_session.movie_session(movie, customers, cleaner)
