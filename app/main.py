from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customer_inst = []
    for customer in customers:
        customer_inst.append(Customer(customer["name"], customer["food"]))

    for customer in customer_inst:
        CinemaBar.sell_product(customer.food, customer)
    hall.movie_session(movie, customer_inst, cleaner)
