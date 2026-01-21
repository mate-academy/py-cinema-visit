from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int,
        cleaner: str, movie: str) -> None:
    new_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for customer in new_customers:
        CinemaBar().sell_product(customer, customer.food)
    CinemaHall(hall_number).movie_session(
        customers=new_customers,
        movie_name=movie,
        cleaning_staff=Cleaner(cleaner)
    )
