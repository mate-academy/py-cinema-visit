from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = [
        Customer(**person) for person in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)

    for person in customer_instances:
        CinemaBar.sell_product(person.food, person)
    cinema_hall.movie_session(movie, customer_instances, cleaner_name)
