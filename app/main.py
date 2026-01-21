from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(
        movie,
        [
            Customer(name=customer_info["name"], food=customer_info["food"])
            for customer_info in customers
        ],
        cleaning_staff
    )
