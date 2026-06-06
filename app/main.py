from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaner_entity = Cleaner(cleaner)
    customer_entities = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customer_entities:
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customer_entities, cleaner_entity)
