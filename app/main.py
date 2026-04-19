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
    instance_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    hall = CinemaHall(hall_number)
    janitor = Cleaner(cleaner)

    for instance_customer in instance_customers:
        CinemaBar.sell_product(instance_customer.food, instance_customer)
    hall.movie_session(
        movie_name=movie,
        customers=instance_customers,
        cleaning_staff=janitor
    )
