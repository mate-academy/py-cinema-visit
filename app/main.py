from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    clients = [
        Customer(name=client["name"], food=client["food"])
        for client in customers
    ]
    cinema = CinemaHall(number=hall_number)
    clean_personal = Cleaner(name=cleaner)
    for client in clients:
        CinemaBar.sell_product(customer=client, product=client.food)
    cinema.movie_session(
        movie_name=movie,
        customers=clients,
        cleaning_staff=clean_personal
    )
