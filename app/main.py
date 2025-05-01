from cinema.bar import CinemaBar
from cinema.hall import CinemaHall
from people.cinema_staff import Cleaner
from people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    instances_customers_list = [Customer(customer.name, customer.food) for customer in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    for customer in instances_customers_list:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, instances_customers_list, cleaner_instance)
