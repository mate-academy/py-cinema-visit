from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customers = [
        Customer(
            customer["name"],
            customer["food"]
        ) for customer in customers
    ]
    cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    for customer in customers:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    cinema_hall.movie_session(
        movie_name=movie, customers=customers, cleaning_staff=cleaner
    )
