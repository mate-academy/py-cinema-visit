from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers, hall_number, cleaner, movie):
    customer_instances = [Customer(name=c['name'], food=c['food']) for c in customers]
    cleaning_staff = Cleaner(name=cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(number=hall_number)
    hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=cleaning_staff)
