from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customers:
        CinemaBar.sell_product(customer, customer.food)
    cinema_hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)

    cinema_hall.movie_session(movie, customers, cleaner_staff)
