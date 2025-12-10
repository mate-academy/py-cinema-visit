from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customers_instances = [Customer(name=c['name'], food=c['food']) for c in customers]
    cinema_hall_instance = CinemaHall(number=hall_number)
    cleaner_instances = Cleaner(name=cleaner)
    for i in customers_instances:
        CinemaBar.sell_product(product=i.food, customer=i)
    cinema_hall_instance.movie_session(movie_name=movie, customers=customers_instances, cleaning_staff=cleaner_instances)
