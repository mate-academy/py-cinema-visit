from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers, hall_number, cleaner, movie):

    customer_objs = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]

    for cust in customer_objs:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall = CinemaHall(hall_number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaner_obj
    )
