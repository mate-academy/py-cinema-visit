from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list[Customer], hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_objects = [Customer(c["name"], c["food"]) for c in customers]
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    hall.movie_session(movie_name=movie,
                       customers=customer_objects, cleaning_staff=cleaner)
