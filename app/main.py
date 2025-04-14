from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    all_customers = [Customer(user["name"], user["food"])
                     for user in customers]
    cinema_bar = CinemaBar()

    for user in all_customers:
        cinema_bar.sell_product(user.food, user)

    personal = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, all_customers, personal)
