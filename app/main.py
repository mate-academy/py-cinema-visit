from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_instances = [Customer(name=customer["name"], food=customer["food"]) for customer in customers]

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number)

    hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=Cleaner(name=cleaner))
