from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)

    for customer_info in customers:
        customer = Customer(name=customer_info["name"], food=customer_info["food"])
        cinema_bar.sell_product(customer=customer, product=customer.food)
        customer.watch_movie(movie=movie)

    cinema_hall.movie_session(movie_name=movie, customers=[Customer(name=customer["name"], food=customer["food"]).watch_movie(movie) for customer in customers], cleaning_staff=cleaner)
