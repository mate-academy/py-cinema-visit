from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    new_customers = []
    for customer in customers:
        new_customers.append(
            Customer(
                customer["name"],
                customer["food"]
            )
        )
    ch = CinemaHall(hall_number)
    cr = Cleaner(cleaner)
    for customer in new_customers:
        CinemaBar.sell_product(customer.food, customer)

    ch.movie_session(
        cleaning_staff=cr,
        movie_name=movie,
        customers=new_customers
    )
