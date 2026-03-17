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
    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            food=customer["food"],
        )

        customer_instances.append(customer_instance)
        CinemaBar.sell_product(
            product=customer_instance.food,
            customer=customer_instance
        )

    hall = CinemaHall(number=hall_number,)
    cleaner = Cleaner(name=cleaner,)

    hall.movie_session(movie, customer_instances, cleaner)
