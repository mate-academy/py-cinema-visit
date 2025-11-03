from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    clients = [Customer(customer["name"], customer["food"])
               for customer in customers]
    for client in clients:
        CinemaBar.sell_product(product=client.food, customer=client)
    hall = CinemaHall(number=hall_number)
    staff = Cleaner(cleaner)
    hall.movie_session(movie_name=movie,
                       customers=clients,
                       cleaning_staff=staff)
