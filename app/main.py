from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    our_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    our_cleaner = Cleaner(cleaner)
    for customer in our_customers:
        CinemaBar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, our_customers, our_cleaner)
