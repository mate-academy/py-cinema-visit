from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = [
        Customer(
            name=c["name"],
            food=c["food"]
        )
        for c in customers
    ]
    cleaning_instance = Cleaner(name=cleaner)
    hall = CinemaHall(number=number)

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_instance
    )
