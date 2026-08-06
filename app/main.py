from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_instances = [
        Customer(name=cust_dict["name"], food=cust_dict["food"])
        for cust_dict in customers
    ]

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    hall.movie_session(movie, customer_instances, cleaning_staff)
