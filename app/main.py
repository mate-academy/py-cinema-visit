from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_obj = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]
    hall_obj = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    for customer in customers_obj:
        CinemaBar.sell_product(customer, customer.food)

    hall_obj.movie_session(
        movie_name=movie,
        customers=customers_obj,
        cleaning_staff=cleaner_obj
    )
