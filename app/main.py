from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer

from app.cinema.bar.py import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customers_list = []

    for customer in customers:
        name = customer["name"]
        food = customer["food"]
        new_customer = Customer(name, food)
        customers_list.append(new_customer)
        CinemaBar.sell_product(new_customer.food, new_customer)
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall.movie_session(movie, customers_list, cleaner_obj)
