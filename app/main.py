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
    """Simulate a cinema visit."""
    customer_objects = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]

    for customer in customer_objects:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
