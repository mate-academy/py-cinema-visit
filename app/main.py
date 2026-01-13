from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objects = [Customer(el["name"], el["food"]) for el in customers]
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)
    hall.movie_session(movie, customer_objects, cleaner)
