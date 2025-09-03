from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:

    customer_objects = []
    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=customer["food"])
        customer_objects.append(customer_obj)

        CinemaBar.sell_product(product=str(customer_obj.food),
                               customer=customer_obj)

    cleaner_obj = Cleaner(name=cleaner)

    hall = CinemaHall(number=hall_number)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj
    )
