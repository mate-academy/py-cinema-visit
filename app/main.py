from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:

    hall = CinemaHall(hall_number)

    cinema_customers = [
        Customer(item["name"], item["food"])
        for item in customers
    ]

    cleaner = Cleaner(cleaner)

    for customer in cinema_customers:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, cinema_customers, cleaner)
