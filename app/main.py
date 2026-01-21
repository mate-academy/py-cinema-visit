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
    customer_obj = []

    for customer_dict in customers:
        customer = Customer(customer_dict["name"], customer_dict["food"])
        customer_obj.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_obj,
        cleaning_staff=cleaner_obj
    )
