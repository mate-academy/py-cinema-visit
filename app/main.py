from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    cb = CinemaBar()
    for customer in customers:
        cb.sell_product(customer=Customer(name=customer["name"],
                                          food=customer["food"]),
                        product=customer["food"])

    ch = CinemaHall(number=hall_number)
    ch.movie_session(movie_name=movie,
                     customers=[Customer(name=customer["name"],
                                         food=customer["food"])
                                for customer in customers],
                     cleaning_staff=Cleaner(cleaner))
