from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    class_customers = [Customer(**customer) for customer in customers]

    for class_customer in class_customers:
        CinemaBar.sell_product(class_customer, class_customer.food)

    cleaner = Cleaner(cleaner)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, class_customers, cleaner)
