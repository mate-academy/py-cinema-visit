from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_objects: list[Customer] = [
        Customer(name=item["name"], food=item["food"]) for item in customers
    ]

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)

    hall.movie_session(movie, customer_objects, staff)
