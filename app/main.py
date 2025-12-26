from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    hall_no = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    customers_in_hall = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    for customer in customers_in_hall:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    CinemaHall.movie_session(
        self=hall_no,
        movie_name=movie,
        customers=customers_in_hall,
        cleaning_staff=cleaner,
    )
