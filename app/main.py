# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:

    customers_of_cinema = []

    for customer in customers:
        person = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer=person, product=person.food)
        customers_of_cinema.append(person)

    hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    hall.movie_session(movie_name=movie,
                       customers=customers_of_cinema,
                       cleaning_staff=cinema_cleaner)
