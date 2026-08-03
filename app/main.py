from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list[dict], hall_number: int, cleaner: str, movie: str) -> None:
    customers_obj = [Customer(customer["name"], customer["food"]) for customer in customers]
    for customer in customers_obj:
        CinemaBar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    hall.movie_session(movie, customers_obj, cleaner)
