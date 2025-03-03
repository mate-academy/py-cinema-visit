from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer

def cinema_visit(customers: list[Customer], hall_number: int, cleaner: Cleaner, movie: str):
    customer_objects = [Customer(c["name"], c["food"]) for c in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customer_objects, cleaning_staff)