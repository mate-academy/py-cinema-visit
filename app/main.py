from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    customer_list = []
    bar = CinemaBar()

    for customer in customers:
        client = Customer(name=customer["name"], food=customer["food"])
        customer_list.append(client)
        bar.sell_product(customer=client, product=client.food)

    update_cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    hall.movie_session(movie, customer_list, update_cleaner)
