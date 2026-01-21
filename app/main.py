from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:
    customer_list = []
    for customer in customers:
        client = Customer(customer["name"], customer["food"])
        customer_list.append(client)
        cinema_bar = CinemaBar()
        cinema_bar.sell_product(client.food, client)
    cleaner_worker = Cleaner(cleaner)
    session = CinemaHall(hall_number)
    session.movie_session(movie, customer_list, cleaner_worker)
