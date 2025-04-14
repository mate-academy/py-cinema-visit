from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    for customer in customers:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, customers, cleaner_staff)
