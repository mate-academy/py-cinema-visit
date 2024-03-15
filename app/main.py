from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def create_customers(customers: list) -> list:
    list_customers = []
    for customer in customers:
        list_customers.append(Customer(customer["name"], customer["food"]))
    return list_customers


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    list_customers = create_customers(customers)
    cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for customer in list_customers:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, list_customers, cleaner)
