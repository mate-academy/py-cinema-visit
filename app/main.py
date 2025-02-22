# write your imports here
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_objects = [Customer(c["name"], c["food"]) for c in customers]
    cleaner_object = Cleaner(cleaner)

    for customer in customer_objects:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_object
    )
