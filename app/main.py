from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = []

    for person in customers:
        inst = Customer(name=person["name"], food=person["food"])
        customer_instances.append(inst)
        CinemaBar.sell_product(product=inst.food, customer=inst)

    hall = CinemaHall(number=hall_number)
    cleaner_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_staff
    )
