from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for customer_data in customers:
        customer = Customer(name=customer_data["name"], food=customer_data["food"])
        CinemaBar.sell_product(customer=customer, product=customer.food)
        hall = CinemaHall(hall_number)
        hall.movie_session(movie_name=movie, customers=[Customer(name=customer_data["name"], food=customer_data["food"]) for customer_data in customers], cleaning_staff=Cleaner(name=cleaner))
