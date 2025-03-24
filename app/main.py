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

    current_customers = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        )
        for customer in customers]

    cinema_hall: CinemaHall = CinemaHall(number=hall_number)
    current_cleaner: Cleaner = Cleaner(name=cleaner)

    for customer in current_customers:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, current_customers, current_cleaner)
