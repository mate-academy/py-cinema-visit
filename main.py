from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customer_objects = []
    for cust_dict in customers:
        customer = Customer(name=cust_dict["name"], food=cust_dict["food"])
        customer_objects.append(customer)

    cleaning_staff = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(number=hall_number)

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )