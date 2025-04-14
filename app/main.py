from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_objects = []
    hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)

    for cust in customers:
        customer_objects.append(Customer(cust["name"], cust["food"]))

    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, customer_objects, cleaner_staff)
