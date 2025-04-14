from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner_name: str,
    movie: str
) -> None:
    customers = [Customer(
        customer["name"],
        customer["food"]
    )
        for customer in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner_name)
    cinema_bar = CinemaBar()
    for customer in customers:
        cinema_bar.sell_product(customer=customer, product=customer.food)
    cinema_hall.movie_session(movie, customers, cleaning_staff)
