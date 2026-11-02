from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner_name: str, movie: str) -> None:
    customer_instances = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]
    hall = CinemaHall(hall_number=hall_number)
    cleaner = Cleaner(name=cleaner_name)

    # Cinema bar sells food to customers without creating an instance of CinemaBar
    for customer in customer_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    # Cinema hall schedules the movie session
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner
    )
