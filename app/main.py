from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: Cleaner, movie: str) -> None:
    customer_obj = [Customer(customer["name"], customer["food"])
                    for customer in customers]
    for customer in customer_obj:
        CinemaBar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, customer_obj, cleaning_staff)
