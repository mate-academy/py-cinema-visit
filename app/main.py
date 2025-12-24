from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cleaning = Cleaner(cleaner)
    list_of_customers = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        list_of_customers.append(new_customer)
        CinemaBar.sell_product(new_customer, new_customer.food)
    CinemaHall(hall_number).movie_session(movie, list_of_customers, cleaning)
