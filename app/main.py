from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customers_objects = []
    for custom in customers:
        customers_objects.append(Customer(custom["name"], custom["food"]))
    for custom_object in customers_objects:
        CinemaBar.sell_product(custom_object.food, custom_object)
    cleaner_person = Cleaner(cleaner)
    CinemaHall(hall_number).movie_session(movie,
                                          customers_objects,
                                          cleaner_person)
