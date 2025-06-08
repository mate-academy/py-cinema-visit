from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> object:
    customer_objects = [Customer(name=customer["name"],
                        food=customer["food"]) for customer in customers]
    cleaner_obj = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number=hall_number)

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall.movie_session(movie_name=movie, customers=customer_objects,
                       cleaning_staff=cleaner_obj)
