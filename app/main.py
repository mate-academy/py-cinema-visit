from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_list = []
    for customer_dict in customers:
        customer = Customer(name=customer_dict["name"],
                            food=customer_dict["food"])
        CinemaBar.sell_product(customer_dict["food"], customer)
        customer_list.append(customer)
    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    hall.movie_session(movie, customer_list, staff)
