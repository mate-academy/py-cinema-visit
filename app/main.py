from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner_name: str,
        movie: str
) -> None:
    cinema_customers = [
        Customer(name=cust["name"],
                 food=cust["food"]) for cust in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)

    for cust in cinema_customers:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    cinema_hall.movie_session(movie, cinema_customers, cleaner)
