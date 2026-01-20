from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:

    just_customers = []
    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data["food"])
        just_customers.append(customer)
        CinemaBar.sell_product(customer_data["food"], customer)

    cinema_hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    cinema_hall.movie_session(movie, just_customers, cleaner_obj)
