from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customer_instances: list[Customer] = []
    for c_data in customers:
        customer = Customer(name=c_data["name"], food=c_data["food"])
        CinemaBar.sell_product(product=customer.food, customer=customer)
        customer_instances.append(customer)

    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaner=cleaner_instance,
    )
