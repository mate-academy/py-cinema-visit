# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    # write you code here
    pass
def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_objects = [
        Customer(
            name=c["name"],
            food=c["food"]
        )
        for c in customers
    ]

    for cust in customer_objects:
        CinemaBar.sell_product(
            product=cust.food,
            customer=cust
        )

    hall = CinemaHall(hall_number=hall_number)

    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )