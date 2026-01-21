from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customer: list, hall_number: int, cleaner: str, movie: str):
    customer_instances = [Customer(name=c["name"], food=c["food"]) for c in customer]
    cleaning_staff = Cleaner(name=cleaner)
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer = customer)
    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=cleaning_staff)


