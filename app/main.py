from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    cinema_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    assigned_cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for customer in cinema_customers:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, cinema_customers, assigned_cleaner)
