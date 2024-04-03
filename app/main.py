from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers = [
        Customer(person["name"], person["food"])
        for person in customers
    ]
    cinema_bar = CinemaBar()
    for customer in customers:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers, cleaner)
