from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> str:
    customer_obj = []
    for customer in customers:
        cust = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(cust.food, cust)
        customer_obj.append(cust)

    cinema_hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customer_obj, clean)
