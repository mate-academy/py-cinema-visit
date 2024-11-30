from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    clients = [Customer(customer["name"], customer["food"])
               for customer in customers]
    [CinemaBar.sell_product(customer.food, customer) for customer in clients]

    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=clients,
        cleaning_staff=Cleaner(cleaner)
    )
