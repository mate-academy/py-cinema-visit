from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customers_list = []
    for man in customers:
        human = Customer(man["name"], man["food"])
        customers_list.append(human)
        CinemaBar.sell_product(human.food, human)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, customers_list, cleaning_staff)
