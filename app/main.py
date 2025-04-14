from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = [
        Customer(client["name"], client["food"])
        for client in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cinema_cleaner = Cleaner(cleaner)

    for client in customer_instances:
        cinema_bar.sell_product(client, client.food)

    cinema_hall.movie_session(movie, customer_instances, cinema_cleaner)
