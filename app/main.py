from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    cinema_customers = []

    for customer in customers:
        cinema_customers.append(Customer(customer["name"], customer["food"]))

    for customer in cinema_customers:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, cinema_customers, cinema_cleaner)
