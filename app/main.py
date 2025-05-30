from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_instances = [Customer(name=customer['name'],
                                   food=customer['food']) for customer in customers]
    cinemahall = CinemaHall(number=hall_number)
    instance_of_cleaner = Cleaner(name=cleaner)
    cinemabar = CinemaBar()

    for customer in customer_instances:
        cinemabar.sell_product(customer=customer,
                               product=customer.food)
    cinemahall.movie_session(movie_name=movie,
                             customers=customer_instances,
                             cleaning_staff=instance_of_cleaner)
