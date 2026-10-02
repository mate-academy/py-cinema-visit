from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:

    # initialization
    customer_list = []
    for customer in customers:
        customer_list.append(Customer(customer["name"], customer["food"]))

    cinema_cleaner = Cleaner(cleaner)

    ch = CinemaHall(hall_number)

    # bar sells food
    for customer in customer_list:
        CinemaBar.sell_product(customer, customer.food)

    #  schedule a movie
    ch.movie_session(movie, customer_list, cinema_cleaner)
