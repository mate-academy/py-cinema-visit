from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    clients = [Customer(customer.get("name"),
                        customer.get("food"))
               for customer
               in customers]
    cinema_hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)

    for client in clients:
        CinemaBar.sell_product(client.food, client)

    cinema_hall.movie_session(clients, hall_number, current_cleaner, movie)
