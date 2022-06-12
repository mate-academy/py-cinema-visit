from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers_list: list,
                 hall_number: int,
                 cleaning_staff: str,
                 movie: str):

    customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers_list
    ]

    cinema_hall = CinemaHall(hall_number)
    bar = CinemaBar()
    cleaner = Cleaner(cleaning_staff)

    for customer in customers:
        bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, customers, cleaner)
