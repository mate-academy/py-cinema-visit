from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int,
        cleaner: str, movie: str
) -> None:
    customers_groups = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for custumer in customers_groups:
        CinemaBar.sell_product(custumer.food, custumer)
    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customers_groups,
        cleaning_staff=Cleaner(cleaner)
    )
