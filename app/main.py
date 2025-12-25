from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_objects = []
    for i in customers:
        customer_objects.append(Customer(name=i["name"], food=i["food"]))

    cleaning_staff = Cleaner(cleaner)

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaning_staff)