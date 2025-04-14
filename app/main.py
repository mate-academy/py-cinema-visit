from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie_name: str
) -> None:
    customer_instances = []
    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)
    bar_instance = CinemaBar()

    for person in customers:
        customer = Customer(name=person["name"], food=person["food"])
        customer_instances.append(customer)
        bar_instance.sell_product(product=customer.food, customer=customer)

    hall.movie_session(
        movie_name=movie_name,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
