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

    viewers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    hall = CinemaHall(hall_number)
    hall_cleaner = Cleaner(cleaner)

    for viewer in viewers:
        CinemaBar.sell_product(product=viewer.food, customer=viewer)

    hall.movie_session(
        movie_name=movie,
        customers=viewers,
        cleaning_staff=hall_cleaner
    )
