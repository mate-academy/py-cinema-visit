from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_list = [Customer(customer["name"], customer["food"])
                      for customer in customers]
    for customer in customers_list:
        CinemaBar.sell_product(customer.name, customer.food)
    clean = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie_name=movie,
                       customers=customers_list,
                       cleaning_staff=clean)
