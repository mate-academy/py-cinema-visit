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

    clients = [Customer(customer["name"], customer["food"])
               for customer in customers]
    movie_session = CinemaHall(number=hall_number)
    staff = Cleaner(cleaner)

    for client in clients:
        CinemaBar.sell_product(client, client.food)

    movie_session.movie_session(
        movie_name=movie,
        customers=clients,
        cleaning_staff=staff
    )
