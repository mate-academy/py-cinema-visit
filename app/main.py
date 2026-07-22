from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_instances = []
    for client in customers:
        customer = Customer(name=client["name"], food=client["food"])
        customer_instances.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)

    staff_cleaner = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=staff_cleaner,
    )
