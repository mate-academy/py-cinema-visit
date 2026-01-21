from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers = [
        Customer(item.get("name"), item.get("food"))
        for item in customers
    ]
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, customers, cleaner)
