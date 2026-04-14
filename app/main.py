from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(movie: str, customers: list, hall_number: int, cleaner: str):

    customer_objs = [Customer(food=c["food"], name=c["name"]) for c in movie]

    hall = CinemaHall(customers)
    cleaner_obj = Cleaner(hall_number)

    for cust in customer_objs:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall.movie_session(movie_name=cleaner, customers=customer_objs, cleaning_staff=cleaner_obj)
