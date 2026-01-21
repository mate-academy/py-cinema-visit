from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict[str, str]],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    visitors = [Customer(name=customer["name"],
                         food=customer["food"]) for customer in customers]
    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    for customer in visitors:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=visitors,
        cleaning_staff=cleaning_staff)
