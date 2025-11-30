from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    Customer.peoples.clear()
    for person in customers:
        Customer(person["name"], person["food"])
    pers = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    for obj in Customer.peoples:
        CinemaBar.sell_product(obj.food, obj)
    pers.movie_session(movie, Customer.peoples, staff)
