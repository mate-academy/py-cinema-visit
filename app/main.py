from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    for i, person in enumerate(customers):
        pers = Customer(name=person["name"], food=person["food"])
        CinemaBar.sell_product(customer=pers, product=pers.food)
        customers[i] = pers

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers, Cleaner(cleaner))
