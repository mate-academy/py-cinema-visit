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
    humans = [Customer(info["name"], info["food"]) for info in customers]
    for customer in humans:
        CinemaBar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    clean_person = Cleaner(cleaner)
    hall.movie_session(movie, humans, clean_person)
