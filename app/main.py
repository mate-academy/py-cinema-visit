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

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    customer_list = []
    for customer_info in customers:
        customer = Customer(customer_info["name"], customer_info["food"])
        customer_list.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customer_list, cleaning_staff)
