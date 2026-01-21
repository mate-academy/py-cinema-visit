from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers, hall_number, cleaner, movie):
    customer_objs = []

    for data in customers:
        cust = Customer(name=data["name"], food=data["food"])
        customer_objs.append(cust)
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(movie_name=movie, customers=customer_objs, cleaning_staff=cleaning_staff)
