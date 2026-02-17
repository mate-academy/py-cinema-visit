from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_objects = []
    for human in customers:
        customer_object = Customer(name=human["name"], food=human["food"])
        customers_objects.append(customer_object)
        CinemaBar.sell_product(
            product=human["food"],
            customer=customer_object
        )

    hall = CinemaHall(number=hall_number)
    cleaning = Cleaner(cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customers_objects,
        cleaning_staff=cleaning
    )
