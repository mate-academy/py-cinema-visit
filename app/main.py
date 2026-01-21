from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    clients = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    cleaner_person = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    for client in clients:
        cinema_bar.sell_product(product=client.food, customer=client)
    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=clients,
        cleaning_staff=cleaner_person
    )
