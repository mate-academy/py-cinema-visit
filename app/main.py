from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar
    list_ = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in list_:
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, list_, cleaner)
