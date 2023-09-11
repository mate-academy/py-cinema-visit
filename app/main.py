from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []
    for info in customers:
        customers_list.append(Customer(info["name"], info["food"]))

    cinema = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for person in customers_list:
        cinema_bar.sell_product(person.food, person)

    cinema.movie_session(movie, customers_list, cleaner)
