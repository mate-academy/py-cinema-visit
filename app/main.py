from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:
    # Create Customer instances
    customer_instances = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    # Sell products at cinema bar (without creating CinemaBar instance)
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Create hall and cleaner instances
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    # Start movie session (this will call watch_movie and clean_hall inside)
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
