from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    customer_objects: list[Customer] = []

    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"], food=customer_data["food"]
        )

        customer_objects.append(customer)

        CinemaBar.sell_product(customer=customer, product=customer.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff,
    )
