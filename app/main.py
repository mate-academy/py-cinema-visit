from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    visitors = [
        Customer(name=person["name"], food=person["food"])
        for person in customers
    ]

    hall = CinemaHall(number=hall_number)
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
