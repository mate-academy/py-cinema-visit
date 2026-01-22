from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[Customer], hall_number: int, cleaner: str, movie: str
) -> None:
    hall = CinemaHall(number=hall_number)
    users = [
        Customer(name=user["name"], food=user["food"]) for user in customers
    ]
    for user in users:
        CinemaBar.sell_product(user.food, user)
    staff_member = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie, customers=users, cleaning_staff=staff_member
    )
