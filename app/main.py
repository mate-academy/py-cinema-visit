from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(name=cleaner)
    customers = [Customer(x["name"], x["food"]) for x in customers]

    for customer in customers:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers,
        cleaning_staff=cleaner
    )
