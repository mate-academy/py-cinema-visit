from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(customers, hall_number, cleaner, movie):
    customer_objs = [Customer(name=c["name"], food=c["food"]) for c in customers]

    for c in customer_objs:
        CinemaBar.sell_product(product=c.food, customer=c)

    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(movie_name=movie, customers=customer_objs, cleaning_staff=cleaning_staff)


