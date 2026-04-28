from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_objects = []
    for cll in customers:
        customer_objects.append(
            Customer(
                name=cll["name"],
                food=cll["food"]
            )
        )
    cleaner_obj = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number)

    for customer in customer_objects:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj
    )
