from app.people import Customer, Cleaner
from app.cinema import CinemaHall, CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objects = [
        Customer(customer["name"],
                 customer["food"]) for customer in customers
    ]

    for customer in customer_objects:
        CinemaBar.sell_product(customer, product=customer.food)

    hall = CinemaHall(hall_number)
    cleaner_object = Cleaner(cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_object
    )
