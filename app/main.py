from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customer_list = []
    clean = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    for one_customer in customers:
        one_customer = Customer(one_customer["name"], one_customer["food"])
        customer_list.append(one_customer)
        CinemaBar.sell_product(one_customer.food, one_customer)
    hall.movie_session(movie, customer_list, clean)
