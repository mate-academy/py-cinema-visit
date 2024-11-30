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
    # Cinema structure
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)

    # People
    cleaning_staff = Cleaner(cleaner)
    customers = [Customer(customer["name"], customer["food"])
                 for customer in customers]

    for customer in customers:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers, cleaning_staff)
