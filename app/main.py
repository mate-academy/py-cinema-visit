from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    """
        Simulates a cinema visit for a group of customers,
        where they buy food and watch a movie.
    """

    customer_instances = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]

    cinema_bar = CinemaBar()
    for customer in customer_instances:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
