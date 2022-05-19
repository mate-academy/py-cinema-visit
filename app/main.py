from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []

    for person in customers:
        customer = Customer(name=person["name"], food=person["food"])
        customers_list.append(customer)
        CinemaBar.sell_product(customer=customer, product=customer.food)

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    cinema_hall.movie_session(movie, customers_list, cleaner)
