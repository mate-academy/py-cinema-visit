from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customers_instances = [
        Customer(person["name"], person["food"])
        for person in customers
    ]

    for customer in customers_instances:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer,
        )

    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customers_instances,
        cleaning_staff=cleaner,
    )
