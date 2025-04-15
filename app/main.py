# write your imports here
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    clients = []
    room = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    for i in customers:
        # clients.append(Customer(key, value))
        customer = Customer(i["name"], i["food"])
        clients.append(customer)
        CinemaBar.sell_product(i["food"], customer)
    # print(clients)
    room.movie_session(movie, clients, staff)


# customers = [
#     {"name": "Bob", "food": "Coca-cola"},
#     {"name": "Alex", "food": "popcorn"}
# ]
# hall_number = 5
# cleaner_name = "Anna"
# movie = "Madagascar"
# cinema_visit(customers=customers, hall_number=hall_number,
# cleaner=cleaner_name, movie=movie)
