from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_isinstance = []
    for customer in customers:
        customer_isinstance.append(
            Customer(name=customer["name"], food=customer["food"])
        )
    cleaner_isinstance = Cleaner(name=cleaner)
    hall_isinstance = CinemaHall(number=hall_number)

    for customer in customer_isinstance:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall_isinstance.movie_session(
        movie_name=movie,
        customers=customer_isinstance,
        cleaning_staff=cleaner_isinstance,
    )
