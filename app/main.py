# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_instances = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        )
        for customer in customers]
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)

    cleaner = Cleaner(name=cleaner)

    for customer in customers_instances:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_instances,
        cleaning_staff=cleaner)
