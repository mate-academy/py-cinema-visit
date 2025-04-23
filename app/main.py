from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(movie, customers, hall_number, cleaner):
    customer_instances = [Customer(name=customer["name"], food=customer["food"]) for customer in customers]
    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=cleaning_staff)