from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> str:
    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    for custom in customers:
        customer = Customer(custom["name"], custom["food"])
        CinemaBar.sell_product(customer.food, customer)
    hall.movie_session(movie, customers, clean)
