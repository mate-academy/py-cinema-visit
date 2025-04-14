from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall = CinemaHall(hall_number)

    cinema_hall.movie_session(movie_name, customers, Cleaner(cleaning_staff))
