from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_objects = []
    for customer_data in customers:
        customer = Customer(name=customer_data["name"], food=customer_data["food"])
        CinemaBar.sell_product(product=customer.food, customer=customer)
        customer_objects.append(customer)

    cinema_hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)
    cinema_hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaner_obj)
