from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    hall = CinemaHall(hall_number)
    customer_objects = []
    for customer in customers:
        new_customer = Customer(name=customer["name"], food=customer["food"])
        customer_objects.append(new_customer)
        CinemaBar.sell_product(new_customer.food, new_customer)
    cleaner_obj = Cleaner(name=cleaner)
    hall.movie_session(movie, customer_objects, cleaner_obj)
