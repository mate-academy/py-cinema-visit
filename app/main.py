from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_obj_list = []
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        customers_obj_list.append(customer_obj)
        CinemaBar.sell_product(customer_obj.food, customer_obj)
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall.movie_session(movie, customers_obj_list, cleaner_obj)
