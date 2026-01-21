from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    customers_new = []
    for customer_dict in customers:
        customer = Customer(customer_dict["name"], customer_dict["food"])
        cinema_bar.sell_product(customer.food, customer)
        customers_new.append(customer)
    cinema_hall.movie_session(movie, customers_new, clean)
