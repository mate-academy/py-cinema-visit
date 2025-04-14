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
    customers = [
        Customer(person["name"], person["food"])
        for person in customers
    ]
    for person in customers:
        CinemaBar.sell_product(person, person.food)

    hall = CinemaHall(hall_number)
    clean_staff = Cleaner(cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customers,
        cleaning_staff=clean_staff
    )
