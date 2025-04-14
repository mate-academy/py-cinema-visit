from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict], hall_number: int, cleaner: str, movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)

    new_customer = [Customer(customer["name"], customer["food"])
                    for customer in customers]
    for customer in new_customer:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, new_customer, clean)
