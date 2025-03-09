from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objects = [
        Customer(name=c["name"], food=c["food"])
        for customer_var in customers
        if "name" in customer_var and "food" in customer_var
    ]
    if not customer_objects:
        print("No valid customers found!")
        return
    for cust in customer_objects:
        CinemaBar.sell_product(customer=cust, product=cust.food)
    hall = CinemaHall(number)
    cleaner_object = Cleaner(cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_object)
