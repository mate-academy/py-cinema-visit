from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    visitors = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    for visitor in visitors:
        CinemaBar.sell_product(product=visitor.food, customer=visitor)

    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie, customers=visitors, cleaning_staff=cleaning_staff
    )
