from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_objs = []
    for customer in customers:
        new_people = Customer(customer["name"], customer["food"])
        customers_objs.append(new_people)
        CinemaBar.sell_product(new_people.food, new_people)

    CinemaHall(hall_number).movie_session(
        movie,
        customers_objs,
        Cleaner(cleaner)
    )
