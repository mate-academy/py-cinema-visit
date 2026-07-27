from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str)\
        -> None:
    customer_instances = []

    for cust_data in customers:
        customer = Customer(name=cust_data["name"], food=cust_data["food"])
        customer_instances.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall.movie_session(movie, customers=customer_instances,
                       cleaning_staff=cleaner_obj
                       )
