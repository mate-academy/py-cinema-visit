from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    inst_customers: list[Customer]
    # inst_cinemabar: list[CinemaBar]
    inst_clener: Cleaner

    inst_customers = []

    for customer in customers:
        inst_customers.append(Customer(name=customer["name"], food=customer["food"]))

    for customer in inst_customers:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    CinemaHall(number=hall_number).movie_session(movie_name=movie, customers=inst_customers, cleaning_staff=Cleaner(cleaner))
















