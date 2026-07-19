from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_object = [Customer(customer["name"],
                       customer["food"]) for customer in customers]
    clean_person = Cleaner(cleaner)
    hall_name = CinemaHall(hall_number)
    for customer in customer_object:
        CinemaBar.sell_product(customer, customer.food)
    hall_name.movie_session(movie, customer_object, clean_person)
