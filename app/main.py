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
    customer_instances = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]

    for person in customer_instances:
        CinemaBar.sell_product(product=person.food, customer=person)

    hall = CinemaHall(number=hall_number)
    staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=staff
    )
