from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers, hall_number, cleaner, movie):
    customer_instances = [Customer(c["name"], c["food"]) for c in customers]
    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    hall.movie_session(movie, customer_instances, cleaner_instance)
