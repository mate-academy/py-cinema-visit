from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_objects = []
    for customer in customers:
        cust = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(cust.food, cust)
        customer_objects.append(cust)
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall.movie_session(movie, customer_objects, cleaner_obj)
