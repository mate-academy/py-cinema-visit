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
    customer_objects = []

    for customer in customers:
        person = Customer(customer["name"], customer["food"])
        customer_objects.append(person)

        CinemaBar.sell_product(person.food, person)

    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    hall.movie_session(movie, customer_objects, cleaner)
