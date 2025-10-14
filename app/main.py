from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        movie: str,
        customers: list[dict[str, str]],
        hall_number: int,
        cleaner: str
) -> None:

    cleaning_staff = Cleaner(name=cleaner)
    customer_objects = [
        Customer(
            name=c["name"],
            food=c["food"]
        )
        for c in customers
    ]

    for customer in customer_objects:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
