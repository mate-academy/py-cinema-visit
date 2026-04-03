from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar


def cinema_visit(cinema_customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers = [Customer(cinema_customer["name"], cinema_customer["food"])
                 for cinema_customer in cinema_customers]

    for customer in customers:
        CinemaBar.sell_product(customer, customer.food)

    hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)
    hall.movie_session(movie, customers, cleaner_name)
