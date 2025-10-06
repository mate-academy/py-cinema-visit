from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    # Create Customer instances
    customer_instances = []
    for customer_data in customers:
        customer_instance = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        customer_instances.append(customer_instance)
    
    # Sell food to customers at the cinema bar
    for customer_instance in customer_instances:
        CinemaBar.sell_product(
            product=customer_instance.food,
            customer=customer_instance
        )
    
    # Create CinemaHall instance
    hall = CinemaHall(number=hall_number)
    
    # Create Cleaner instance
    cleaning_staff = Cleaner(name=cleaner)
    
    # Schedule movie session
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )