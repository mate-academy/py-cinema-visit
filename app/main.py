from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_objs = [
        Customer(customer_dict["name"], customer_dict["food"])
        for customer_dict in customers
    ]
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    for customer in customer_objs:
        CinemaBar.sell_product(customer, customer.food)
    hall.movie_session(movie, customer_objs, cleaning_staff)
