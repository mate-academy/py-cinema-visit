from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customers = [
        Customer(customer_dict["name"], customer_dict["food"])
        for customer_dict in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)
    for customer in customers:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customers, cleaner)
