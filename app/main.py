from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(film: str, people: list, hall_num: int, cleaner: str) -> None:
    customer_objs = []
    for person in people:
        customer = Customer(name=person["name"], food=person["food"])
        CinemaBar.sell_product(product=customer.food, customer=customer)
        customer_objs.append(customer)
    cleaner_pers = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_num)
    hall.movie_session(movie_name=film, customers=customer_objs, cleaning_staff=cleaner_pers)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(movie, customers, hall_number, cleaner_name)
