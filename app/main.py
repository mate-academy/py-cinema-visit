from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(movie, customers, hall_number, cleaner):
    # Process customers correctly from customers list
    customer_instances = [Customer(name=c["name"], food=c["food"]) for c in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=cleaner_instance)
