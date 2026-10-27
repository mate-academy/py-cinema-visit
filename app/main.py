from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    
    customer_instances = []
    for cust_data in customers:
        customer = Customer(name=cust_data["name"], food=cust_data["food"])
        customer_instances.append(customer)
        
        
        CinemaBar.sell_product(customer=customer, product=customer.food)

    
    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    
    hall.movie_session(
        movie_name=movie, 
        customers=customer_instances, 
        cleaning_staff=cleaning_staff
    )
