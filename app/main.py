from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    ls_of_customers = []
    for customer in customers:
        ls_of_customers.append(
            Customer(customer["name"], customer["food"])
        )

    hall = CinemaHall(hall_number)
    bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for customer in ls_of_customers:
        bar.sell_product(customer, customer.food)

    hall.movie_session(movie, ls_of_customers, cleaner)
