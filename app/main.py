from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_of_customers = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        list_of_customers.append(customer)
    hall_num = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    for customer in list_of_customers:
        cinema_bar.sell_product(customer.food, customer)
    hall_num.movie_session(movie, list_of_customers, cleaner)
