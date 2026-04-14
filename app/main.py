from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(movie: str, customers: list, hall_number: int, cleaner: str):

    customer_objs = [Customer(food=c["food"], name=c["name"]) for c in customers]


    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)


    for cust in customer_objs:
        CinemaBar.sell_product(product=cust.food, customer=cust)


    hall.movie_session(movie_name=movie, customers=customer_objs, cleaning_staff=cleaner_obj)
