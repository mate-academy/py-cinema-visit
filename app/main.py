from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    movie: str, customers: list, hall_number: int, cleaner: str
) -> None:
    customer_instances = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]

    cleaner_instance = Cleaner(name=cleaner)
    hall_instance = CinemaHall(hall_number=hall_number)

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
