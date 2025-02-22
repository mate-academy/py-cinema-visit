from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_instances = [
        Customer(data["name"], data["food"])
        for data in customers
    ]

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer.name)

    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)

    hall.movie_session(
        movie_name=movie, customers=customer_instances, cleaning_staff=staff
    )
