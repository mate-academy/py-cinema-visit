from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_objects = []
    for customer_data in customers:
        new_customer = Customer(customer_data["name"], customer_data["food"])
        customer_objects.append(new_customer)
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    for customer_obj in customer_objects:
        CinemaBar.sell_product(product=customer_obj.food, customer=customer_obj)
    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaner_obj)
