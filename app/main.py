from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cust_inst_list = []
    for customer in customers:
        cust_inst_list.append(Customer(customer['name'], customer['food']))
    for customer in cust_inst_list:
        CinemaBar.sell_product(customer.food, customer)
    clean_staff = Cleaner(cleaner)
    cin_hall = CinemaHall(hall_number)
    cin_hall.movie_session(movie, cust_inst_list, clean_staff)
