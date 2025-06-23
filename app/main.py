from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cleaner import Cleaner

def cinema_visit(customers: list, hall_number: int, cleaner_name: str, movie: str):
    customer_objs = [Customer(name=c["name"], food=c["food"]) for c in customers]

    for c in customer_objs:
        CinemaBar.sell_product(product=c.food, customer=c)

    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner_name)

    hall.movie_session(movie_name=movie, customers=customer_objs, cleaning_staff=cleaning_staff)


