# write your imports here
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str, movie: str
) -> None:

    list_of_customers = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for customer in list_of_customers:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, list_of_customers, cleaner)
