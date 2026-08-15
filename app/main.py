from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    # 1. Create instances
    customer_instances = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]
    cinema_hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    # 2. Cinema bar sells food to customers
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # 3. Movie session runs and triggers cleaning afterwards
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff,
    )
