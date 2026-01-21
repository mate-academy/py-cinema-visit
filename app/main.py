# main.py
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    # Create instances of Customer and Cleaner
    customer_instances = [Customer(name=c['name'], food=c['food']) for c in customers]
    cleaner_instance = Cleaner(name=cleaner)

    # Sell food to customers using CinemaBar class (without instantiating)
    for customer in customer_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    # Create CinemaHall instance
    cinema_hall = CinemaHall(hall_number)

    # Schedule the movie session
    cinema_hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=cleaner_instance)

