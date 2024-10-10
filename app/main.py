from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_list = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for customer in customer_list:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customer_list, cleaner)
