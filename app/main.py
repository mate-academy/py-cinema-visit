from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_hall = CinemaHall(hall_number)
    customers_objects = []
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        customers_objects.append(customer_obj)
        CinemaBar.sell_product(customer_obj.food, customer_obj)
    cinema_hall.movie_session(movie, customers_objects, Cleaner(cleaner))
