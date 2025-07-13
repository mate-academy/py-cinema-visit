from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_objects = []
    for customer_data in customers:
        customer_instance = Customer(name=customer_data["name"], food=customer_data["food"])
        customer_objects.append(customer_instance)
        CinemaBar.sell_product(customer=customer_instance, product=customer_data["food"])

    cleaner_instance = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number=hall_number)
    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaner_instance)
