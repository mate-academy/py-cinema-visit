from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    cinema_bar = CinemaBar()
    for person in customers:
        customer = Customer(person["name"], person["food"])
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=[
            Customer(person["name"], person["food"]) for person in customers
        ],
        cleaning_staff=cleaner_instance
    )
