from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
):
        cinema_hall = CinemaHall(hall_number)
        cleaner = Cleaner(cleaner)
        customer_objects = []

        for customer in customers:
            person = Customer(customer["name"], customer["food"])
            customer_objects.append(person)
            CinemaBar.sell_product(person.food, person)

        cinema_hall.movie_session(movie,customer_objects, cleaner)

