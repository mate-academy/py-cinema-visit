from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict], hall_number: int, cleaner: str, movie: str
) -> None:
    customers_instances = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    hall_instance = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)
    for customer_instance in customers_instances:
        CinemaBar.sell_product(
            product=customer_instance.food, customer=customer_instance
        )
    hall_instance.movie_session(
        movie_name=movie,
        customers=customers_instances,
        cleaning_staff=cleaner_instance
    )
