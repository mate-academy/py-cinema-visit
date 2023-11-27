from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str, movie: str) -> None:
    for person in customers:
        customer = Customer(person["name"], person["food"])
        CinemaBar.sell_product(product=customer.food, customer=customer)
    CinemaHall(hall_number).movie_session(
        movie_name=movie,
        customers=[Customer(customer["name"], customer["food"])
                   for customer in customers],
        cleaning_staff=Cleaner(cleaner)
    )
