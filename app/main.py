from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_customers = [
        Customer(
            customer["name"],
            customer["food"]
        )
        for customer in customers
    ]
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in list_customers:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, list_customers, cleaner)
