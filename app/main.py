from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objects = []
    for customer in customers:
        customer_objects.append(Customer(customer["name"], customer["food"]))

    hall = CinemaHall(number)
    cleaner = Cleaner(cleaner)
    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, customer_objects, cleaner)
