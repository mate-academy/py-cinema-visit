from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str, movie: str) -> None:

    customers_list = [
        Customer(customer_dict["name"], customer_dict["food"])
        for customer_dict in customers
    ]

    cinema_bar = CinemaBar()

    for customer in customers_list:
        cinema_bar.sell_product(customer, customer.food)

    hall_number_instance = CinemaHall(hall_number)

    staff_instance = Cleaner(cleaner)

    hall_number_instance.movie_session(movie, customers_list, staff_instance)
