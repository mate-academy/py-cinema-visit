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

    customer_objects = [Customer(**c_dict) for c_dict in customers]
    cleaner_object = Cleaner(name=cleaner)
    hall_object = CinemaHall(number=hall_number)

    for customer in customer_objects:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    return hall_object.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_object
    )
