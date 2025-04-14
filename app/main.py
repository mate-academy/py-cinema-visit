from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    if customers:

        clients = []
        for client in customers:
            clients.append(Customer(
                name=client.get("name"),
                food=client.get("food")
            )
            )

        hall = CinemaHall(hall_number)
        cinema_cleaner = Cleaner(cleaner)

        for customer in clients:
            CinemaBar.sell_product(customer, customer.food)

        hall.movie_session(movie, clients, cinema_cleaner)
