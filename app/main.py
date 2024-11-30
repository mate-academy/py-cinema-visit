from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    customer_instances = []
    for customer in customers:
        customer_instance = Customer(name=customer["name"],
                                     food=customer["food"])
        cinema_bar.sell_product(product=customer_instance.food,
                                customer=customer_instance)
        customer_instances.append(customer_instance)

    cinema_hall.movie_session(movie_name=movie,
                              customers=customer_instances,
                              cleaning_staff=cleaner_instance)
