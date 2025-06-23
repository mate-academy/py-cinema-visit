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

    customer_list = []
    for customer in customers:
        customer_inst = Customer(customer["name"], customer["food"])
        customer_list.append(customer_inst)
        CinemaBar.sell_product(customer_inst.food, customer_inst)
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    hall.movie_session(movie, customer_list, cleaner)
