from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customer_instances = []
    for customer in customers:
        customer_instance = Customer(
            name=customer["name"], food=customer["food"]
        )
        customer_instances.append(customer_instance)

    for customer in customer_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=Cleaner(cleaner),
    )
