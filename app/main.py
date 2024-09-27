from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)

    customer_instances = [Customer(customer_data["name"],
                                   customer_data["food"])
                          for customer_data in customers]

    for customer in customer_instances:
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customer_instances, cinema_cleaner)
