from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    instances = []
    for instance in customers:
        name = instance["name"]
        food = instance["food"]
        my_instance = Customer(name, food)
        CinemaBar.sell_product(my_instance, food)
        instances.append(my_instance)

    my_hall = CinemaHall(hall_number)
    my_cleaner = Cleaner(cleaner)
    my_hall.movie_session(movie, instances, my_cleaner)
