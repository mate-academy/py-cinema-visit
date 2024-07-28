from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaning_staff: str,
    movie_name: str
) -> None:
    cinema_hall = CinemaHall(number=hall_number)

    customer_objects = []
    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        customer_objects.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(
        movie_name=movie_name,
        customers=customer_objects,
        cleaning_staff=Cleaner(name=cleaning_staff)
    )
