from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:
    cb = CinemaBar()
    customer_s = []

    for i, customer in enumerate(customers):
        customer, product = customer.values()
        i = Customer(customer, product)
        customer_s.append(i)
        cb.sell_product(customer=i.name, product=i.food)

    CinemaHall(hall_number).movie_session(movie, customer_s, Cleaner(cleaner))
