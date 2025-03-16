from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    list_of_customers = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    for customer in list_of_customers:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, list_of_customers, cinema_cleaner)
