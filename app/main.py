from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cleaner_object = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    customers_objects = []
    for customer in customers:
        customers_objects.append(Customer(customer["name"], customer["food"]))
    for customer in customers_objects:
        CinemaBar.sell_product(customer, customer.food)
    hall.movie_session(movie, customers_objects, cleaner_object)
