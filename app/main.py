from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie_name: str
) -> None:
    customer_instances = [Customer(c["name"], c["food"]) for c in customers]
    hall = CinemaHall(hall_number)
    bar_cinema = CinemaBar()
    cleaning_staff = Cleaner(cleaner)

    for customer in customer_instances:
        bar_cinema.sell_product(customer.food, customer)

    hall.movie_session(movie_name, customer_instances, cleaning_staff)
