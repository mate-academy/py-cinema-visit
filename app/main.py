from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict], hall_number: int, cleaner: str, movie: str) ->None:
    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)
    customers_instances = []
    for customer in customers:
        (customers_instances.append(Customer(name=customer["name"], food=customer["food"])))
    for customer in customers_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall.movie_session(movie_name=movie, customers=customers_instances, cleaning_staff=cleaner_instance)
