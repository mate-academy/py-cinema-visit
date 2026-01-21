from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[Customer],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customers_list = []
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_staff = Cleaner(cleaner)

    for customer_info in customers:
        customer = Customer(customer_info["name"], customer_info["food"])
        customers_list.append(customer)
        cinema_bar.sell_product(customer, customer.food)

    hall.movie_session(movie, customers_list, cleaner_staff)
