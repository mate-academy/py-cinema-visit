from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customer_object = []
    for customer_data in customers:
        customer_obj = Customer(name=customer_data["name"],
                                food=customer_data["food"])
        customer_object.append(customer_obj)
    for customer in customer_object:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    cleaner = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(
        movie_name=movie, customers=customer_object, cleaning_staff=cleaner
    )
