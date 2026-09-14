from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    clients = []
    for customer in customers:
        clients.append(Customer(name=customer["name"], food=customer["food"],))
    cleaner_staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    for client in clients:
        CinemaBar.sell_product(product=client.food, customer=client)
    hall.movie_session(movie_name=movie,
                       customers=clients,
                       cleaning_staff=cleaner_staff)
