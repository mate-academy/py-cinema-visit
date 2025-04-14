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
    customers_list = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)
    hall_instance.movie_session(movie, customers_list, cleaner_instance)
