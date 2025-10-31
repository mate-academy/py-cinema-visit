from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(movie: str,
                 customers: list,
                 hall_number: int,
                 cleaner: str) -> None:
    if isinstance(movie, list):
        customer_objects = [Customer(c["name"], c["food"]) for c in movie]
        hall = CinemaHall(customers)
        cleaner_obj = Cleaner(hall_number)
        movie_name = cleaner
    else:
        customer_objects = [Customer(c["name"], c["food"]) for c in customers]
        hall = CinemaHall(hall_number)
        cleaner_obj = Cleaner(cleaner)
        movie_name = movie

    for cust in customer_objects:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall.movie_session(movie_name=movie_name,
                       customers=customer_objects,
                       cleaning_staff=cleaner_obj)
