from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers, hall_number, cleaner, movie):
    # Create instances of Customer, CinemaHall, and Cleaner
    customer_instances = [Customer(name=customer["name"], food=customer["food"]) for customer in customers]
    cleaner_instance = Cleaner(name=cleaner)
    hall_instance = CinemaHall(hall_number=hall_number)

    # Sell products to customers using keyword arguments
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Schedule the movie session
    hall_instance.movie_session(movie_name=movie,
                                customers=customer_instances,
                                cleaning_staff=cleaner_instance)

