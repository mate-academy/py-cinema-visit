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

    customers_list = []

    for customer_dict in customers:
        customer = Customer(
            customer_dict["name"],
            customer_dict["food"]
        )
        customers_list.append(customer)

    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)

    hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_instance
    )
