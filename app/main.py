from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_objs = [
        Customer(name=person["name"],
                 food=person["food"]) for person in customers
    ]
    cleaner_obj = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)

    for customer in customer_objs:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaner_obj
    )
