from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str) -> None:

    customers = [Customer(name=customer["name"], food=customer["food"])
                 for customer in customers]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()

    for customer in customers:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    cinema_hall.movie_session(movie_name=movie_name,
                              customers=customers,
                              cleaning_staff=Cleaner(cleaning_staff))
