from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_obj = [Customer(element["name"],
                              element["food"]) for element in customers]
    for element in customers_obj:
        CinemaBar.sell_product(element, element.food)
    red_hall = CinemaHall(hall_number)
    alisa = Cleaner(cleaner)
    red_hall.movie_session(movie, customers_obj, alisa)
