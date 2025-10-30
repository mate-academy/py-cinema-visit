from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customers_ = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    cleaner_ = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for customer in customers_:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, customers_, cleaner_)
