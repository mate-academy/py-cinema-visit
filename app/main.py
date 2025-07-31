from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cust_res = []
    for customer in customers:
        cust_instance = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(cust_instance.food, cust_instance)
        cust_res.append(cust_instance)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, cust_res, cleaning_staff)
