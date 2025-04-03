from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int,
                 cleaner_name: str, movie: str) -> str:

    customer_objects = []
    for customer_data in customers:
        customer_name = customer_data["name"]
        food = customer_data["food"]
        customer = Customer(customer_name, food)
        customer_objects.append(customer)

    cinema_bar = CinemaBar()
    for customer in customer_objects:
        product = customer.food
        cinema_bar.sell_product(customer, product)

    cleaner = Cleaner(cleaner_name)
    cinemahall = CinemaHall(hall_number)
    movie_name = movie
    cinemahall.movie_session(movie_name, customer_objects, cleaner)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 8
cleaner_name = "Anna2"
movie = "Madagascar3"
cinema_visit(customers=customers, hall_number=hall_number,
             cleaner_name=cleaner_name, movie=movie)
