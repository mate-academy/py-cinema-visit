from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = [
        Customer(person["name"], person["food"])
        for person in customers
    ]
    cleaning_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for person in customers_list:
        CinemaBar.sell_product(person.food, person)

    cinema_hall.movie_session(movie, customers_list, cleaning_staff)
