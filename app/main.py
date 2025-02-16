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
    customer_objects = [Customer(**customer) for customer in customers]
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)
    hall.movie_session(movie, customer_objects, cleaner_obj)
