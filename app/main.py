from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str)\
        -> None:
    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)
    customer_instances = []
    for customer in customers:
        (customer_instances.append
         (Customer(name=customer["name"], food=customer["food"])))
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall.movie_session(movie_name=movie, customers=customer_instances,
                       cleaning_staff=cleaner_instance)
