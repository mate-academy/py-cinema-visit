from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict[str, str]],
                 hall_number: int,
                 cleaner_name: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)

    for customer_info in customers:
        customer = Customer(customer_info["name"], customer_info["food"])
        cinema_bar.sell_product(customer, customer.food)

    hall.movie_session(
        movie,
        [Customer(customer_info["name"],
                  movie) for customer_info in customers],
        cleaner
    )
