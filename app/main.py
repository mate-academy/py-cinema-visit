from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_objects = [Customer(c["name"], c["food"]) for c in customers]
    cleaner_obj = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for cust in customer_objects:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaner_obj)
