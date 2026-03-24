from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_instances = []
    for person_data in customers:
        customer = Customer(person_data["name"], person_data["food"])
        CinemaBar.sell_product(customer.food, customer)
        customer_instances.append(customer)

    cleaner_instance = Cleaner(cleaner)
    hall_instance = CinemaHall(hall_number)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
