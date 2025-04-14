from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    all_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    our_cleaner = Cleaner(cleaner)

    for customer in all_customers:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, all_customers, our_cleaner)
