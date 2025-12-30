from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    # create Customer instances from input dicts
    customer_objs = [Customer(c['name'], c['food']) for c in customers]

    # sell products via CinemaBar (static method)
    for cust in customer_objs:
        CinemaBar.sell_product(customer=cust, product=cust.food)

    # create CinemaHall and Cleaner instances
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    # run movie session
    hall.movie_session(movie, customer_objs, cleaning_staff)
