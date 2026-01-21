from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cust_name_food = [Customer(customer["name"], customer["food"]
                               ) for customer in customers]
    cleaner = Cleaner(cleaner)
    hall_number = CinemaHall(hall_number)
    customers_list = []
    for customer in cust_name_food:
        customer = Customer(customer, customer.food)
        customers_list.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer.name)
    CinemaHall.movie_session(hall_number, movie, cust_name_food, cleaner)
