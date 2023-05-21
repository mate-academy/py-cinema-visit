from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for customer_dict in customers:
        customer = Customer(
            customer_dict["name"],
            customer_dict["food"]
        )
        cinema_bar.sell_product(customer, customer.food)

    customer_instances = [
        Customer(cust["name"], cust["food"]) for cust in customers
    ]
    hall.movie_session(movie, customer_instances, cleaning_staff)
