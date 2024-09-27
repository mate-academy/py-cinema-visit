from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str, movie:
        str) -> None:
    customers = [
        Customer(
            customer["name"],
            food=customer["food"]
        ) for customer in customers
    ]
    cleaner = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(hall_number)
    for customer in customers:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    cinema_hall.movie_session(
        movie_name=movie, customers=customers, cleaning_staff=cleaner
    )
