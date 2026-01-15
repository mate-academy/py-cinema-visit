from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_instances = [Customer(c["name"], c["food"]) for c in customers]
    cleaner_instance = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie_name=movie,
                       customers=customer_instances,
                       cleaning_staff=cleaner_instance)
