from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    customers_objects = [Customer(c["name"], c["food"])for c in customers]
    cleaning_staff = Cleaner(cleaner)
    for customer in customers_objects:
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(number=hall_number)
    hall.movie_session(movie, customers_objects, cleaning_staff)
