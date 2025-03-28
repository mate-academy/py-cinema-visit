from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(movie, customers, hall_number, cleaner):
    cleaner_instance = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number=hall_number)
    customer_instances = [Customer(name=c['name'], food=c['food']) for c in customers]

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=cleaner_instance)
    cleaner_instance.clean_hall(hall_number) 
