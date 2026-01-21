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
    list_of_customers = []
    for element in customers:
        customer = Customer(element["name"], element["food"])
        CinemaBar.sell_product(customer, customer.food)
        list_of_customers.append(customer)

    CinemaHall(hall_number).movie_session(
        movie,
        list_of_customers,
        Cleaner(cleaner)
    )
