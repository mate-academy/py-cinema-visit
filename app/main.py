from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    hall = CinemaHall(number=hall_number)
    bar_obg = CinemaBar()
    stuff = Cleaner(cleaner)
    customers_list = [
        Customer(name=customer_data["name"], food=customer_data["food"])
        for customer_data in customers
    ]
    for customer in customers_list:
        bar_obg.sell_product(customer, product=customer.food)
    hall.movie_session(movie, customers_list, stuff)
