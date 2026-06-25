from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customers_instance = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    cinema_hall_instance = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    for customer in customers_instance:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    cinema_hall_instance.movie_session(
        movie_name=movie,
        customers=customers_instance,
        cleaning_staff=cleaner_instance,
    )
