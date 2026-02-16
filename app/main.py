from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cleaner_obj = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    customers_list = []

    for customer_dict in customers:
        customer = Customer(name=customer_dict.get("name"), food=customer_dict.get("food"))
        CinemaBar.sell_product(product=customer.food, customer=customer)
        customers_list.append(customer)
    cinema_hall.movie_session(movie_name=movie, customers=customers_list, cleaning_staff=cleaner_obj)

