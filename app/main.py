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
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customers_ = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customers_:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers_, cleaner)
