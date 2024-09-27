from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str, movie: str
) -> None:
    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    client = [
        Customer(cust.get("name"), cust.get("food")) for cust in customers
    ]
    for cust in client:
        CinemaBar.sell_product(cust, cust.food)
    hall.movie_session(movie, client, clean)
