# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    # creating instances
    customer_objects = [Customer(c["name"], c["food"]) for c in customers]
    cinema_bar = CinemaBar()
    cleaner_staff = Cleaner(cleaner)

    # implementation of cinema work
    for customer in customer_objects:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customer_objects, cleaner_staff)
