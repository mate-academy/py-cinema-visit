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
    customers_class = [
        Customer(person["name"], person["food"]) for person in customers
    ]
    for person in customers_class:
        CinemaBar.sell_product(person.food, person)

    janitor = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_class, janitor)
