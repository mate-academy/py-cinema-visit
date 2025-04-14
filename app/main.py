from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(customers, hall_number, cleaner, movie):
    # Create instances of Customer
    customer_objects = [Customer(name=c['name'], food=c['food']) for c in customers]

    # Sell products to customers
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Create CinemaHall and Cleaner instances
    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    # Start movie session
    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaner_instance)
