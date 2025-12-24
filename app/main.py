from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    list_of_customers = []

    for customer in customers:
        list_of_customers.append(Customer(customer["name"], customer["food"]))

    today_cleaner = Cleaner(cleaner)

    for customer in list_of_customers:
        CinemaBar.sell_product(customer, customer.food)

    CinemaHall(hall_number).movie_session(
        movie,
        list_of_customers,
        today_cleaner
    )
