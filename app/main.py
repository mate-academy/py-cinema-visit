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
    current_customers = [
        Customer(person["name"], person["food"])
        for person in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)

    for person in current_customers:
        CinemaBar.sell_product(person, person.food)

    cinema_hall.movie_session(
        movie,
        current_customers,
        current_cleaner
    )
