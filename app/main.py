from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(movie: str,
                 customers: list,
                 hall_number: int,
                 cleaner: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaner_object = Cleaner(name = cleaner)
    clients = []
    for customer in customers:
        clients.append(Customer(name = customer["name"], food = customer["food"]))
    for client in clients:
        CinemaBar.sell_product(product = client.food, customer = client)
    cinema_hall.movie_session(movie_name = movie, customers = clients, cleaning_staff = cleaner_object)