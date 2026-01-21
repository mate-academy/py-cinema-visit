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
    customers = [Customer(info["name"], info["food"]) for info in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for customer in customers:
        cinema_bar.sell_product(customer, product=customer.food)

    cinema_hall.movie_session(movie, customers, cleaning_staff)
