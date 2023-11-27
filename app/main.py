from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customers = []
    for customer in customers:
        list_of_customers.append(
            Customer(customer["name"], customer["food"])
        )
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for guest in list_of_customers:
        cinema_bar.sell_product(guest.food, guest)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=cleaning_staff
    )
