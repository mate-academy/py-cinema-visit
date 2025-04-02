from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_bar = CinemaBar()
    customers_list = [Customer(name=customer["name"], food=customer["food"])
                      for customer in customers]
    for man in customers_list:
        cinema_bar.sell_product(man, man.food)
    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    hall.movie_session(movie, customers_list, clean)
