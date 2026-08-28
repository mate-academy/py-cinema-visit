from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customers_ = [Customer(name=c["name"], food=c["food"]) for c in customers]

    for customer in customers_:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customers_,
        cleanning_staff=Cleaner(name=cleaner)
    )
