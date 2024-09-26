from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[Customer],
    hall_number: int,
    cleaning_staff: str,
    movie_name: str,
) -> str:
    customers = [
        Customer(person["name"], person["food"])
        for person in customers
    ]

    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)

    for customer in customers:
        CinemaBar().sell_product(customer=customer, product=customer.food)
    hall.movie_session(movie_name, customers, cleaner)
