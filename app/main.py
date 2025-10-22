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
    hall.movie_session(film, customer_objs, cleaner_pers)
