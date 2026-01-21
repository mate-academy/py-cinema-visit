from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaning_staff: str,
                 movie: str) -> None:
    customers_list = [Customer(
        name=customer["name"],
        food=customer["food"]
    ) for customer in customers]

    hall = CinemaHall(number=hall_number)

    cleaner = Cleaner(name=cleaning_staff)

    for customer in customers_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner)
