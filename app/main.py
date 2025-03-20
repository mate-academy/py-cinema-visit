from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_of_customers = []
    cinema_hall = CinemaHall(hall_number)
    clean_staff = Cleaner(cleaner)
    for name in customers:
        customer = Customer(name["name"], name["food"])
        list_of_customers.append(customer)
        CinemaBar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, list_of_customers, clean_staff)
