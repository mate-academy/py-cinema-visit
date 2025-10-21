from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customer_objs = []
    for person in customers:
        customer = Customer(name=person["name"], food=person["food"])
        CinemaBar.sell_product(product=customer.food, customer=customer)
        customer_objs.append(customer)
    cleaner_obj = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    hall.movie_session(movie_name=movie, customers=customer_objs, cleaning_staff=cleaner_obj)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers, hall_number, cleaner_name, movie)