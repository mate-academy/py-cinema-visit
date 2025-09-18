from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(movie, customers, hall_number, cleaner):
    # 1) build Customer objects
    customer_objs = [Customer(c["name"], c["food"]) for c in customers]

    # 2) sell food via static method on the class
    for cust in customer_objs:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    # 3) prepare hall and Cleaner
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    # 4) run session and cleanup using keywords
    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaner_obj
    )
