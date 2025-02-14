from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_objects = [Customer(c["name"], c["food"]) for c in customers]
    cleaner_object = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(movie, customer_objects, cleaner_object)
