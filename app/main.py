from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaning_staff: str,
                 movie: str) -> None:
    new_customers = [
        Customer(person["name"], person["food"]) for person in customers
    ]
    cleaner = Cleaner(cleaning_staff)
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    for customer in new_customers:
        cinema_bar.sell_product(customer.food, customer)
    hall.movie_session(movie, new_customers, cleaner)
