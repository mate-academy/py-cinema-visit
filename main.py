from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar

customers = [{"name": "Bob", "food": "Coca-cola"},
             {"name": "Alex", "food": "popcorn"}]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"


def cinema_visit(movie: str, customers: list, hall_number: int,
                 cleaner: str) -> None:
    customers_combined = []
    for customer in customers_combined:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    for customer in customers:
        customers_combined.append(Customer(customer["name"], customer["food"]))
    cleaner = Cleaner(cleaner)
    ch = CinemaHall(hall_number)
    ch.movie_session(movie_name=movie, customers=customers_combined, cleaning_staff=cleaner)


cinema_visit(customers=customers,
             hall_number=hall_number, cleaner=cleaner_name, movie=movie)
