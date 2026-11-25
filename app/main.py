from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    audience = [
        Customer(name=person["name"], food=person["food"])
        for person in customers
    ]
    for customer in audience:
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, audience, Cleaner(cleaner))
