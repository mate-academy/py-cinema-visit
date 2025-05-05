from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    real_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    hall = CinemaHall(hall_number)
    cleaning_person = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for customer in real_customers:
        cinema_bar.sell_product(customer, customer.food)

    hall.movie_session(movie, real_customers, cleaning_person)
