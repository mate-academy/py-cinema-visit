from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaning_staff: Cleaner | str,
                 movie_name: str) -> None:
    person_list = []
    for person_params in customers:
        person = Customer(person_params["name"],
                          person_params["food"])
        person = person
        person_list.append(person)

        CinemaBar.sell_product(person, person.food)
    customers = person_list
    cinema = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaning_staff)

    cinema.movie_session(movie_name,
                         customers,
                         cleaning_staff)
