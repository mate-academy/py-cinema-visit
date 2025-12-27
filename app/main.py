from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> str:
    customer_objects = [
        Customer(name=customer["name"],
                 food=customer["food"])
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner_info = Cleaner(name=cleaner)

    for customer, data in zip(customers, customer_objects):
        CinemaBar.sell_product(data.food, data)

    cinema_hall.movie_session(movie, customer_objects, cleaner_info)
