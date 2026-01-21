from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_list = []
    cinemabar = CinemaBar()

    for customer in customers:
        customer_name = Customer(customer["name"], customer["food"])
        cinemabar.sell_product(customer_name, customer["food"])
        customers_list.append(customer_name)

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    cinema_hall.movie_session(movie, customers_list, cleaning_staff)
