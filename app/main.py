from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_list = []

    for custom in customers:
        customer = Customer(custom["name"], custom["food"])
        customer_list.append(customer)

    hall = CinemaHall(hall_number)

    cleaning_staff = Cleaner(cleaner)

    for customer in customer_list:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, customer_list, cleaning_staff)
