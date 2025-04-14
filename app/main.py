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
    all_customers = []
    for i in customers:
        i["name"] = Customer(i["name"], i["food"])
        CinemaBar.sell_product(i["name"], i["name"].food)
        all_customers.append(i["name"])

    hall_number = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    hall_number.movie_session(movie, all_customers, cleaner_staff)
