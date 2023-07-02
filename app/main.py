from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_clients = [Customer(
        client["name"],
        client["food"])
        for client in customers]

    for client in cinema_clients:
        CinemaBar.sell_product(customer=client,
                               product=client.food)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=cinema_clients,
        cleaning_staff=Cleaner(cleaner)
    )

