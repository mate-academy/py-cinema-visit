from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    hall = CinemaHall(hall_number)
    cleaner_peop = Cleaner(cleaner)
    customer_object = [
        Customer(person["name"], person["food"])
        for person in customers
    ]
    for person in customer_object:
        CinemaBar.sell_product(product=person.food, customer=person)
    hall.movie_session(movie, customer_object, cleaner_peop)
