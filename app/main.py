from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    real_customers = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]
    hall = CinemaHall(hall_number)
    real_cleaner = Cleaner(cleaner)
    for customer in real_customers:
        CinemaBar.sell_product(customer.food, customer)
    hall.movie_session(movie, real_customers, real_cleaner)
