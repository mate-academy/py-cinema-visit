from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    customer_instance = [Customer(name=customer["name"], food=customer["food"]) for customer in customers]

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    for customer in customer_instance:
        cinema_bar.sell_product(customer=customer.name, product=customer.food)

    cinema_hall.movie_session(movie_name=movie, customers=customer_instance, cleaning_staff=cleaner_instance)

