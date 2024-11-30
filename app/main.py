from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict], hall_number: int, cleaner: str, movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    customers_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cleaner = Cleaner(cleaner)
    for customer in customers_list:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customers_list, cleaner)
