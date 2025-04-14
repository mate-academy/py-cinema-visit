from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = [
        Customer(
            name=customer.get("name"),
            food=customer.get("food")
        ) for customer in customers
    ]
    hall_instance = CinemaHall(
        number=hall_number
    )
    cleaner_instance = Cleaner(
        name=cleaner
    )
    bar_instance = CinemaBar()

    for customer in customers_list:
        bar_instance.sell_product(customer.food, customer)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_instance
    )
