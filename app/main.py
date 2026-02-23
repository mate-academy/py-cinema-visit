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

    created = []

    for item in customers:
        customer = Customer(name=item["name"], food=item["food"])
        CinemaBar.sell_product(product=customer.food, customer=customer)
        created.append(customer)

    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie, customers=created, cleaning_staff=cleaning_staff
    )
