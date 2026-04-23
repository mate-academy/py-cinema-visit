from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_instances = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
