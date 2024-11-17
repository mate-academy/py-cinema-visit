from app.people.customer import Customer
from app.cinima.bar import CinemaBar
from app.cinima.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        movie: str,
        customers: Customer,
        hall_number: int,
        cleaner: Cleaner
) -> None:

    customer_objects = [
        Customer(name=c["name"],
                 food=c["food"]) for c in customers
    ]

    cleaner_instance = Cleaner(name=cleaner)

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cinema_hall = CinemaHall(number=hall_number)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_instance
    )
