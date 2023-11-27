from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[Customer],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaners = Cleaner(cleaner)

    for customer in customer_list:
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customer_list, cleaners)
