from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:
    customer_instances = []
    bar_object = CinemaBar()
    for person in customers:
        pers = Customer(person["name"], person["food"])
        customer_instances.append(pers)
        bar_object.sell_product(pers.food, pers)

    hall_object = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)
    hall_object.movie_session(movie_name, customer_instances, cleaner)
