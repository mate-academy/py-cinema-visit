from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    movie: str,
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,

) -> None:
    customer_objects = []
    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )

        customer_objects.append(customer)
        CinemaBar.sell_product(customer, customer.food)

    cleaner = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner
    )
