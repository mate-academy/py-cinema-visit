from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, number: int, cleaner: str, movie: str
) -> None:
    customer_object = [Customer(
        name=c["name"], food=c["food"]
    ) for c in customers]

    for cust in customer_object:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    cleaner_staff = Cleaner(name=cleaner)

    cinema_hall = CinemaHall(number=number)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_object,
        cleaning_staff=cleaner_staff
    )
