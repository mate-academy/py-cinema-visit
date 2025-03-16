from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str,
):
    customer_objects = [Customer(c["name"], c["food"]) for c in customers]
    hall = CinemaHall(hall_number)
    cleaner_object = Cleaner(cleaner)

    for customer in customer_objects:
        CinemaBar.sell_product(customer, customer.food)

    hall.movie_session(movie, customer_objects, cleaner_object)

