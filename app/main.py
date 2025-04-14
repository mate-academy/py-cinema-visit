from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    visitors = []
    for customer in customers:
        visitor = Customer(
            name=customer.get("name"),
            food=customer.get("food")
        )
        CinemaBar.sell_product(customer=visitor, product=visitor.food)
        visitors.append(visitor)

    cleaner = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(hall_number)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=visitors,
        cleaning_staff=cleaner
    )
