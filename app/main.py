from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)
    customers = [Customer(**visitor) for visitor in customers]

    for customer in customers:
        cinema_bar.sell_product(
            customer=customer,
            product=customer.food
        )

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers,
        cleaning_staff=cleaner
    )
