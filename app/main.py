from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_list = []
    for i in customers:
        customers_i = Customer(i["name"], i["food"])
        CinemaBar.sell_product(i["food"], customers_i)
        customers_list.append(customers_i)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    CinemaHall.movie_session(hall, movie, customers_list, cleaning_staff)
