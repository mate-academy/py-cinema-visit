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
    clients = []
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for customer in customers:
        client = Customer(customer.get("name"), customer.get("food"))
        CinemaBar.sell_product(client, client.food)
        clients.append(client)

    cinema_hall.movie_session(movie, clients, cleaning_staff)
