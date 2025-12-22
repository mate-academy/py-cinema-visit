from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    clients = []
    current_cleaner = Cleaner(cleaner)
    for customer in customers:
        clients.append(Customer(
            name=customer.get("name"),
            food=customer.get("food")
        ))
    for client in clients:
        CinemaBar.sell_product(customer=client, product=client.food)
    cinema_hall_object = CinemaHall(hall_number)
    cinema_hall_object.movie_session(movie, clients, current_cleaner)
