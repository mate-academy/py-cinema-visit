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
    cinema_hall = CinemaHall(hall_number)
    cinema_customers = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]
    cinema_cleaner = Cleaner(cleaner)
    for customer in cinema_customers:
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, cinema_customers, cinema_cleaner)
