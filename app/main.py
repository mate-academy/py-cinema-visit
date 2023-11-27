from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    hall = CinemaHall(hall_number)
    list_of_customers = []
    cleaner = Cleaner(cleaner)
    for customer in customers:
        list_of_customers.append(Customer(customer["name"], customer["food"]))
    cb = CinemaBar()
    for customer in list_of_customers:
        cb.sell_product(customer, customer.food)
    hall.movie_session(movie, list_of_customers, cleaner)
