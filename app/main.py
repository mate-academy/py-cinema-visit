from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    customer_objects = []
    for data in customers:
        customer_obj = Customer(name=data["name"], food=data["food"])
        customer_objects.append(customer_obj)
        bar.sell_product(customer=customer_obj, product=customer_obj.food)

    hall.movie_session(movie, customer_objects, cleaner_obj)
