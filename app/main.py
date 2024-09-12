from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    customer_instances = [Customer(element["name"], element["food"])
                          for element in customers]

    for person in customer_instances:
        cinema_bar.sell_product(person.food, person)
    cinema_hall.movie_session(movie, customer_instances, cleaning_staff)
