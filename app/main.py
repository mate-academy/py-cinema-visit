from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    movie: str,
    customers: list[dict],
    hall_number: int,
    cleaner: str
) -> None:
    if isinstance(movie, list) and isinstance(customers, int):
        movie, customers, hall_number, cleaner = (
            cleaner,
            movie,
            customers,
            hall_number
        )

    visitors = [
        Customer(name=person["name"], food=person["food"])
        for person in customers
    ]

    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    for customer in visitors:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    hall.movie_session(
        movie_name=movie,
        customers=visitors,
        cleaning_staff=cleaning_staff
    )
