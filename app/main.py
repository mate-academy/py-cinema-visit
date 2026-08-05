from app.people import Customer, Cleaner
from app.cinema import CinemaHall, CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str,
        ) -> None:
    customer_object = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customer_object:
        CinemaBar.sell_product(
            customer,
            product=customer.food,
        )

    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_object,
        cleaning_staff=clean)
