from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(customers: list, number: int, cleaner: str, movie: str) -> None:
    customer_objects = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
        if "name" in c and "food" in c
    ]
    if not customer_objects:
        print("No valid customers found!")
        return
    for cust in customer_objects:
        CinemaBar.sell_product(customer=cust)
    hall = CinemaHall(number)
    cleaner_object = Cleaner(cleaner)
    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaner_object)
