from app.cinema.bar import  CinemaBar
from app.cinema.hall import  CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_list = [Customer(name=i["name"], food=i["food"]) for i in customers]
    cinema_hall = CinemaHall(hall_number)
    clean_person = Cleaner(cleaner)
    for customer1 in customer_list:
        CinemaBar.sell_product(product=customer1.food, customer=customer1)
    cinema_hall.movie_session(movie, customer_list, clean_person)
