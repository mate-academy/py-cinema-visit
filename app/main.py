from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    # Initialize required infrastructure
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    # Create customers and sell them food
    visitors = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        visitors.append(customer)
        cinema_bar.sell_product(customer, customer.food)

    # Make a movie session
    cinema_hall.movie_session(movie, visitors, cleaner)
