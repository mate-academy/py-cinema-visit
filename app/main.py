from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers, hall_number, cleaner, movie):
    cleaner_instance = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    customer_instances = []

    for c in customers:
        cust = Customer(name=c["name"], food=c["food"])
        customer_instances.append(cust)
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
