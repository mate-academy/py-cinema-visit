from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers, hall_number, cleaner, movie):
    customer_instances = []
    for customer in customers:
        customer_instance = Customer(name=customer["name"], food=customer["food"])
        CinemaBar.sell_product(customer=customer_instance, product=customer_instance.food)
        customer_instances.append(customer_instance)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
