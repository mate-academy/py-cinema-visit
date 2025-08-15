from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str,
) -> None:
    customer_list = []
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer_instance.food, customer_instance)
        customer_list.append(customer_instance)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, customer_list, cleaning_staff)
