from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)

    customers_instances = []
    for person in customers:
        name = person.get("name")
        food = person.get("food")
        attender = Customer(name, food)
        CinemaBar.sell_product(food, attender)
        customers_instances.append(attender)

    cinema.movie_session(movie, customers_instances, cinema_cleaner)
