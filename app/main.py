from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_list = []
    for people in customers:
        customer_instance = Customer(people["name"], people["food"])
        customer_list.append(customer_instance)
    movie_hall = CinemaHall(hall_number)
    hall_cleaner = Cleaner(cleaner)
    cb = CinemaBar()
    for customer in customer_list:
        cb.sell_product(customer, customer.food)
    movie_hall.movie_session(movie, customer_list, hall_cleaner)
