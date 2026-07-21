from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_objects = [
        Customer(**customer_dict)
        for customer_dict in customers
    ]

    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaning_staff = Cleaner(name=cleaner)

    for customer in customer_objects:
        cinema_bar.sell_product(product=customer.food, customer=customer)
    cinema_hall.movie_session(movie, customer_objects, cleaning_staff)
