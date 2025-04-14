from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    customer_obj_list: list[Customer] = []
    for customer in customers:
        customer_obj_list.append(Customer(customer["name"], customer["food"]))
        cinema_bar.sell_product(
            customer_obj_list[-1].food,
            customer_obj_list[-1]
        )

    cinema_hall.movie_session(movie, customer_obj_list, cleaner)
