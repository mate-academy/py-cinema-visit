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

    clients: list = [
        Customer(
            name=customer.get("name"),
            food=customer.get("food")
        ) for customer in customers
    ]

    for client in clients:
        CinemaBar.sell_product(customer=client, product=client.food)

    CinemaHall(number=hall_number).movie_session(
        move_name=movie,
        customers=clients,
        cleaning_staff=Cleaner(name=cleaner)
    )
