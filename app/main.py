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
    cinema_bar = CinemaBar
    cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    customers = [
        Customer(
            customer["name"],
            customer["food"]
        )
        for customer in customers
    ]
    for customer in customers:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, list(customers), cleaner)
