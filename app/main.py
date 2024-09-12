from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    customer_objs = []
    for person in customers:
        customer = Customer(person["name"], person["food"])
        cinema_bar.sell_product(customer.food, customer)
        customer_objs.append(customer)

    hall.movie_session(movie, customer_objs, cleaner)
