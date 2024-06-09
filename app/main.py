from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict], hall_number: int, cleaner: str,
                 movie: str) -> None:
    customer_objs = [Customer(name=c["name"], food=c["food"])
                     for c in customers]
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_obj = Cleaner(cleaner)

    for customer in customer_objs:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(movie_name=movie, customers=customer_objs,
                       cleaning_staff=cleaner_obj)
