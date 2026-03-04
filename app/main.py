from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_list: list[Customer] = []
    for customer in customers:
        customer_obj = Customer(
            name=customer["name"],
            food=customer["food"]
        )
        customer_list.append(customer_obj)
    for customer_l in customer_list:
        CinemaBar.sell_product(customer_l.food, customer_l)
    hall = CinemaHall(hall_number)
    cinema_staff = Cleaner(cleaner)
    hall.movie_session(movie, customer_list, cinema_staff)
