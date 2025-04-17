from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_objs = [
        Customer(
            name=c["name"],
            food=c["food"])
        for c in customers
    ]

    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)

    for customer in customer_objs:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=staff
    )
