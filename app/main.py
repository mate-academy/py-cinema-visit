from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_list = []
    for customer_dict in customers:
        customer = Customer(customer_dict["name"], customer_dict["food"])
        customer_list.append(customer)

        CinemaBar.sell_product(customer.food, customer)
    cleaning_staff = Cleaner(cleaner)

    cinema = CinemaHall(hall_number)
    cinema.movie_session(movie, customer_list, cleaning_staff)
