from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_objects = []
    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data["food"])
        customer_objects.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)
    cinema_hall = CinemaHall(hall_number)
    cleaner_object = Cleaner(cleaner)
    cinema_hall.movie_session(movie_name=movie,
                              customers=customer_objects,
                              cleaning_staff=cleaner_object)
