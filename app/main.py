from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    customers_list = [Customer(person["name"], person["food"])
                      for person in customers]
    for customer in customers:
        CinemaBar.sell_product(customer["name"], customer["food"])

    cleaner_name = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_list, cleaner_name)
