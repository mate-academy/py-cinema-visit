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
    customers = [
        Customer(name=guest["name"], food=guest["food"])
        for guest in customers
    ]

    for customer in customers:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    staff = Cleaner(name=cleaner)

    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers,
        cleaning_staff=staff
    )
