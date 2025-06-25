from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = []
    for customer_data in customers:
        customer_instance = Customer(
            name=customer_data["name"], food=customer_data["food"])
        customer_instances.append(customer_instance)

    cleaner_instance = Cleaner(name=cleaner)

    cinema_hall_instance = CinemaHall(number=number)

    for customer_inst in customer_instances:
        CinemaBar.sell_product(
            product=customer_inst.food, customer=customer_inst)

    cinema_hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
