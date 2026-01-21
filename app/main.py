from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: str,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    bar_cinema = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    customer_objs = []

    for customer in customers:
        name = customer["name"]
        food = customer["food"]
        customer_obj = Customer(name, food)
        bar_cinema.sell_product(customer_obj, food)
        customer_objs.append(customer_obj)

    cinema_hall.movie_session(movie, customer_objs, cleaner_obj)
