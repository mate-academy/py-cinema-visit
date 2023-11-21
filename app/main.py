from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_objects = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)
    for customer in customers_objects:
        CinemaBar.sell_product(
            customer=customer,
            product=customer.food
        )
    hall.movie_session(
        movie_name=movie,
        customers=customers_objects,
        cleaning_staff=cleaner_instance
    )
