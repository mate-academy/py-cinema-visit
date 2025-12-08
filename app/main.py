from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers, hall_number, cleaner, movie):
    # Create Customer instances
    customer_instances = []
    for customer_data in customers:
        customer = Customer(name=customer_data["name"], food=customer_data["food"])
        customer_instances.append(customer)

    # Sell products to customers
    for customer in customer_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    # Create CinemaHall and Cleaner instances
    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    # Start movie session
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
