from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    # Create instances of Customer, CinemaHall, and Cleaner
    customer_instances = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]
    cinema_hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    # The cinema bar sells food to customers
    for customer in customer_instances:
        CinemaBar.sell_product(
            product=customer.food, customer=customer
        )

    # Schedule the movie session
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance,
    )
