from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_list = []

    for customer in customers:
        customer_list.append(
            Customer(customer["name"], customer["food"])
        )
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    for customer in customer_list:
        CinemaBar.sell_product(customer.food, customer)
    hall.movie_session(movie, customer_list, cleaning_staff)
