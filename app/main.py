from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    clients = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        )
        for customer in customers
    ]

    cleaner_instance = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(number=hall_number)

    for customer in clients:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=clients,
        cleaning_staff=cleaner_instance
    )
