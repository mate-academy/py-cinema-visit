from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customer_instances = []

    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"],
        )
        customer_instances.append(customer)
        CinemaBar.sell_product(
            customer=customer,
            product=customer.food,
        )
    cleaner_instance = Cleaner(name=cleaner)
    hall_instance = CinemaHall(number=hall_number)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance,
    )
