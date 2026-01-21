from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    new_cleaner = Cleaner(cleaner)
    list_of_customers = []
    for person in customers:
        person.__repr__()
        list_of_customers.append(Customer(
            name=person["name"], food=person["food"]))
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    for person in list_of_customers:
        cinema_bar.sell_product(product=person.food, customer=person.name)
    cinema_hall.movie_session(
        movie_name=movie, customers=list_of_customers, cleaner=new_cleaner)
