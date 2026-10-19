from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customers_in_list = []
    for person in customers:
        new_person = Customer(person["name"], person["food"])
        customers_in_list.append(new_person)
        CinemaBar.sell_product(person["food"], new_person)

    cleaning_staff_after_movie = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(
        movie, customers_in_list, cleaning_staff_after_movie)
