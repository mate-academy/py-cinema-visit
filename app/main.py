from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    obj_customers = [
        Customer(person["name"], person["food"])
        for person in customers
    ]

    for customer in obj_customers:
        CinemaBar.sell_product(customer, customer.food)

    CinemaHall(hall_number).movie_session(
        movie, obj_customers , Cleaner(cleaner)
    )
