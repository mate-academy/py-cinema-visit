from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    clients = []

    for client in customers:
        customer = Customer(client.get("name"), client.get("food"))
        CinemaBar.sell_product(product=customer.food, customer=customer)
        clients.append(customer)

    session_cleaner = Cleaner(name=cleaner)

    CinemaHall(hall_number).movie_session(
        movie_name=movie,
        customers=clients,
        cleaning_staff=session_cleaner
    )
