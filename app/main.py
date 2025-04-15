from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cb = CinemaBar()
    customers_list = [Customer(person["name"], person["food"])
                      for person in customers]
    for per in customers_list:
        cb.sell_product(customer=per, product=per.food)
    cleaner_person = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_list, cleaner_person)
