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
    array = []
    for i in range(len(customers)):
        array.append(Customer(customers[i]["name"], customers[i]["food"]))
        CinemaBar.sell_product(array[i], array[i].food)

    number = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    CinemaHall.movie_session(number, movie, array, cleaner)
