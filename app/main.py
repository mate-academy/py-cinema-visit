from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str)\
        -> None:

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    customers_obj = []
    for customer in customers:
        customers_obj.append(Customer(customer["name"], customer["food"]))
        cinema_bar.sell_product(customers_obj[-1].food, customers_obj[-1])

    cinema_hall.movie_session(movie, customers_obj, cleaner)
