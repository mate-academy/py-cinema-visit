from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(movie, customers, hall_number, cleaner):
    customer_objects = [Customer(name=c["name"], food=c["food"]) for c in customers]

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaner_obj)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "AI Buddy"
movie = "Mad Vlad"

cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie)