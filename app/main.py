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
    customers_list = []
    for customer in customers:
        customers_list.append(Customer(customer["name"], customer["food"]))

    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    staff = Cleaner(cleaner)

    for person in customers_list:
        cinema_bar.sell_product(person, person.food)

    hall.movie_session(movie, customers_list, staff)
