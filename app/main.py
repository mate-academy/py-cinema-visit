from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()

    customer_instances = [
        Customer(name=customer["name"],
                 food=customer["food"]) for customer in customers
    ]

    for customer in customer_instances:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall = CinemaHall(number=hall_number)

    cinema_hall.movie_session(movie_name=movie,
                              customers=customer_instances,
                              cleaning_staff=Cleaner(name=cleaner))
