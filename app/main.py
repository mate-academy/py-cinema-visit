from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:

    customer_instances = []
    for person_data in customers:
        person = Customer(person_data["name"], person_data["food"])
        CinemaBar.sell_product(person.food, person)
        customer_instances.append(person)

    cinema_hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    cinema_hall_instance.movie_session(movie, customer_instances,
                                       cleaner_instance)
