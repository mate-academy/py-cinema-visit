from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_instances = []

    for customer_info in customers:
        customer = Customer(
            name=customer_info["name"],
            food=customer_info["food"],
        )
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer,
        )
        customer_instances.append(customer)

    cinema_hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance,
    )
