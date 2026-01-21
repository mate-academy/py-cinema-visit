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
    cb = CinemaBar()
    ch = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customer_objects = [
        Customer(name=c["name"],
                 food=c["food"])
        for c in customers
    ]
    for customer in customer_objects:
        cb.sell_product(product=customer.food, customer=customer)
    ch.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner
    )
