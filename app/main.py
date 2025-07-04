from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str)\
        -> None:
    customer_instances = []
    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=customer["food"])
        customer_instances.append(customer_obj)
        CinemaBar.sell_product(
            product=customer_obj.food, customer=customer_obj
        )

    hall = CinemaHall(number=hall_number)

    cleaner_obj = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie, customers=customer_instances,
        cleaning_staff=cleaner_obj
    )
