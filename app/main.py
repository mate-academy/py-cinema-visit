from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    all_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_bar = CinemaBar()

    for customer in all_customers:
        cinema_bar.sell_product(customer, customer.food)

    personal = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, all_customers, personal)
