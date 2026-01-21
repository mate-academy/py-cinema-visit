from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> str:
    list_custom = []

    for client in customers:
        visitor = Customer(client["name"], client["food"])
        list_custom.append(visitor)
        CinemaBar.sell_product(visitor.food, visitor)

    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    hall.movie_session(movie, list_custom, clean)
