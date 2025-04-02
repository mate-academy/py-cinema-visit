from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    # Create Cleaner_instance
    cleaner_instance = Cleaner(name=cleaner)
    # Create Customer_instance
    customer_instances = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]
    # Cinema bar sells food to customers
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    # Cinema hall schedules movie session
    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaner=cleaner_instance
    )
