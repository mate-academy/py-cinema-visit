from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_instances = [Customer(person["name"],
                                    person["food"])
                           for person in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for person in customers_instances:
        CinemaBar.sell_product(person.food, person)

    cinema_hall.movie_session(movie_name=movie,
                              customers=customers_instances,
                              cleaning_staff=cleaner)
