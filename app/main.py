from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:
    customer_instances = [Customer(name=guest["name"],
                                   food=guest["food"]) for guest in customers]

    hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(name=cleaning_staff)

    for customer in customer_instances:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(movie_name=movie_name,
                       customers=customer_instances,
                       cleaning_staff=cleaner)
