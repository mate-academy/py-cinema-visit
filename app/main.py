from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    hall = CinemaHall(hall_number)
    worker = Cleaner(cleaner)
    customer_instances = [Customer(customer["name"], customer["food"]) for customer in customers]

    for customer_instance in customer_instances:
        CinemaBar.sell_product(customer_instance.food, customer_instance)

    hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=worker)

    worker.clean_hall(hall_number)






