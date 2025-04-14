from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    # Create instances of CinemaBar, CinemaHall, and Cleaner
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    # Sell food to customers
    for customer_info in customers:
        customer_instance = Customer(name=customer_info["name"], food=customer_info["food"])
        cinema_bar.sell_product(customer=customer_instance, product=customer_instance.food)

    # Start movie session
    cinema_hall.movie_session(movie_name=movie, customers=[Customer(**customer) for customer in customers], cleaning_staff=cleaner_instance)


# Example usage:
customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"

cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie)
