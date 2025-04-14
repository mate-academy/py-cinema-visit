
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_class = []
    for customer in customers:
        customer_temp = Customer(customer["name"], customer["food"])
        customers_class.append(customer_temp)
        CinemaBar.sell_product(customer_temp, customer_temp.food)
    clean = Cleaner(cleaner)
    CinemaHall(hall_number).movie_session(movie, customers_class, clean)
