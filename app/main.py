from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    customer_instances = [Customer(**customer) for customer in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    for customer in customer_instances:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customer_instances, cleaner_instance)
