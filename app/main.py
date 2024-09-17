from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict], hall_number: int, cleaner: str, movie: str
) -> None:

    list_customer = [
        Customer(person["name"], person["food"])
        for person in customers
    ]

    bar_production = CinemaBar()
    cleaner = Cleaner(cleaner)
    hall_number = CinemaHall(hall_number)

    for customer in list_customer:
        bar_production.sell_product(customer.food, customer)

    hall_number.movie_session(movie, list_customer, cleaner)
