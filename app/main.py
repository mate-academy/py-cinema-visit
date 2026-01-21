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
    customer_objs = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        ) for customer in customers
    ]
    cleaner_obj = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for customer in customer_objs:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaner_obj
    )
