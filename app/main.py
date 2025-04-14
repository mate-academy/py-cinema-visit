from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    customer_objects = []
    for customer_data in customers:
        customer = Customer(name=customer_data["name"], food=customer_data["food"])
        customer_objects.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)
    cinema_hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaner_instance)

