from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_objects = [Customer(name=customer["name"], food=customer["food"])
                        for customer in customers]
    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for customer in customer_objects:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(movie_name=movie, customers=customer_objects,
                       cleaning_staff=cleaner_instance)
