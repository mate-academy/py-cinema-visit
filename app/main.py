from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_of_customers = []

    for customer in customers:
        list_of_customers.append(Customer(customer["name"], customer["food"]))
    cinema_hall = CinemaHall(hall_number)
    bar = CinemaBar()
    clean = Cleaner(cleaner)

    for customer in list_of_customers:
        bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, list_of_customers, clean)
