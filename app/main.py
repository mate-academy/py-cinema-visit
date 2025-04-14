from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    visitors = list()

    for customer in customers:
        visitors.append(Customer(customer["name"], customer["food"]))

    hall = CinemaHall(hall_number)
    wiper = Cleaner(cleaner)

    for person in visitors:
        CinemaBar.sell_product(person.food, person)

    hall.movie_session(movie, visitors, wiper)
