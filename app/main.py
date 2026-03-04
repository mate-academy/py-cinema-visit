from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:

    customer_obj = []

    for customer in customers:
        customer_instance = Customer(name=customer["name"],
                                     food=customer["food"])
        customer_obj.append(customer_instance)

        CinemaBar.sell_product(customer=customer_instance,
                            product=customer_instance.food)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(movie_name=movie,
                       customers=customer_obj,
                       cleaning_staff=cleaner_obj)
