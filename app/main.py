from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customers = [Customer(c["name"], c["food"]) for c in customers]
    cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, customers, cleaner)
