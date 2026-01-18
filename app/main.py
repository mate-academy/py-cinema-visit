import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(movie, customers, hall_number, cleaner):
    customer_instances = [Customer(name=customer["name"], food=customer["food"]) for customer in customers]

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for customer in customer_instances:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=cleaning_staff)