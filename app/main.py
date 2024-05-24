from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customers_instance = []

    for customer in customers:
        human = Customer(name=customer["name"], food=customer["food"])
        customers_instance.append(human)
        cinema_bar.sell_product(human.food, human)

    cinema_hall.movie_session(
        movie_name=movie, customers=customers_instance, cleaning_staff=cleaner
    )
