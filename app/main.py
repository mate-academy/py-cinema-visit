from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(movie, customers, hall_number, cleaner):
    customer_list = []
    for c in customers:
        customer_obj = Customer(c["name"], c["food"])
        CinemaBar.sell_product(product=customer_obj.food, customer=customer_obj)
        customer_list.append(customer_obj)
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall.movie_session(movie_name=movie, customers=customer_list, cleaning_staff=cleaner_obj)
