from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        number: int,
        cleaner: str,
        movie: str,
) -> None:

    customer_objects = [
        Customer(name=c["name"],
                 food=c["food"])
        for c in customers]

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cleaner_obj = Cleaner(name=cleaner)
    hall = CinemaHall(number=number)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj
    )
