from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_new = [Customer(customer.get("name"),
                             customer.get("food")) for customer in customers]

    for man in customer_new:
        CinemaBar.sell_product(man.food, man)

    cleaner_name = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customer_new, cleaner_name)
