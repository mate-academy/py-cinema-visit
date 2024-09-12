from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:

    list_of_customer = []
    cinema_bar = CinemaBar()

    for cust in customers:
        customer = Customer(cust["name"], cust["food"])
        list_of_customer.append(customer)
        cinema_bar.sell_product(product=cust["food"], customer=customer)

    CinemaHall(hall_number).movie_session(
        movie,
        list_of_customer,
        Cleaner(cleaner)
    )
