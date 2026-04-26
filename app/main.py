from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_instances = [Customer(c["name"], c["food"]) for c in customers]

    cinema_hall = CinemaHall(hall_number)

    the_cleaner = Cleaner(cleaner)

    for i in range(len(customers)):
        CinemaBar.sell_product(customers[i]["food"], customer_instances[i])

    cinema_hall.movie_session(movie, customer_instances, the_cleaner)
