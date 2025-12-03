from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(movie: str, customers: list, hall_number: int, cleaner: str):
    customer_objects = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]
    cleaner_object = Cleaner(name=cleaner)
    hall_object = CinemaHall(hall_number=hall_number)

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall_object.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_object
    )
