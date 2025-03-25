from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    visitors = []

    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=customer["food"])
        visitors.append(customer_obj)
        CinemaBar.sell_product(customer_obj.food, customer_obj)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    hall.movie_session(movie, visitors, cleaning_staff)
