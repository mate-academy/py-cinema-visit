from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    result = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        result.append(new_customer)
    for visitor in result:
        CinemaBar.sell_product(visitor.food, visitor)
    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    hall.movie_session(movie, result, clean)
