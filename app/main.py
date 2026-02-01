from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customer_instances = []
    for customer_data in customers:
        new_customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"])
        customer_instances.append(new_customer)

    cleaner_instance = Cleaner(name=cleaner)

    hall_instance = CinemaHall(number=hall_number)

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
