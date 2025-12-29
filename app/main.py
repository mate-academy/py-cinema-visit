from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner




def cinema_visit(movie, customers, hall_number, cleaner):
    customer_objects = []

    for data in customers:
        customer = Customer(data["name"], data["food"])
        customer_objects.append(customer)
        CinemaBar.sell_product(customer, data["food"])

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(movie, customer_objects, cleaner_obj)