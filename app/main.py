from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(movie: str, customers: list, hall_number: int, cleaner: str) -> None:
    customer_object = []
    for data in customers:
        customer = Customer(name = data["name"], food = data["food"])
        customer_object.append(customer)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(name = cleaner)

    for customer in customer_object:
        CinemaBar.sell_product(product = customer.food, customer = customer)

    hall.movie_session(movie_name = movie, customers = customer_object, cleaning_staff = cleaner_obj)
