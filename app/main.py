from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[object],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    new_customers_list = [Customer(customer["name"], customer["food"])
                          for customer in customers]
    for new_cinema_bar in new_customers_list:
        CinemaBar.sell_product(new_cinema_bar, new_cinema_bar.food)
    cleaning_staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, new_customers_list, cleaning_staff)
