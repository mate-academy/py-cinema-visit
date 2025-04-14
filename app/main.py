from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    customers_list = []
    for customer in customers:
        cust = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(cust.food, cust)
        customers_list.append(cust)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_list, Cleaner(cleaner))
