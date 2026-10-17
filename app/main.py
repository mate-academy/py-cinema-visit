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
    customers_list: list = []

    for key, customer in enumerate(customers):
        new_customer = Customer(customer["name"], customer["food"])
        customers_list.append(new_customer)

        CinemaBar.sell_product(new_customer, new_customer.food)

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    cinema_hall.movie_session(movie, customers_list, cleaning_staff)
