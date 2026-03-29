from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    customer_objects = []
    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=customer["food"])
        customer_objects.append(customer_obj)
        CinemaBar.sell_product(customer_obj.food, customer_obj)

    hall.movie_session(movie, customer_objects, cleaner_obj)
