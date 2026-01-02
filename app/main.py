from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list | Customer, hall_number: int, cleaner: str, movie: str):
    customer_list = []
    for cust in customers:
        customer_list.append(Customer(cust["name"], cust["food"]))
    cinema_hall1 = CinemaHall(hall_number)
    cleaner1 = Cleaner(cleaner)

    for i in range(len(customer_list)):
        CinemaBar.sell_product(customer_list[i])
    cinema_hall1.movie_session(movie, customer_list, cleaner1)
