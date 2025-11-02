from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(movie: str,
                 customers: list,
                 hall_number: int,
                 cleaner: str) -> None:
    clients = [Customer(customer["name"], customer["food"])
               for customer in customers]
    for client in clients:
        CinemaBar.sell_product(product=client.food, customer=client)
    hall = CinemaHall(number=hall_number)
    staff = Cleaner(cleaner)
    hall.movie_session(movie_name=movie,
                       customers=clients,
                       cleaning_staff=staff)

# customers = [
#     {"name": "Bob", "food": "Coca-cola"},
#     {"name": "Alex", "food": "popcorn"}
# ]
# hall_number = 5
# cleaner_name = "Anna"
# movie = "Madagascar"
# cinema_visit(customers=customers, hall_number=hall_number,
# cleaner=cleaner_name, movie=movie)
# Cinema bar sold Coca-cola to Bob.
# Cinema bar sold popcorn to Alex.
# "Madagascar" started in hall number 5.
# Bob is watching "Madagascar".
# Alex is watching "Madagascar".
# "Madagascar" ended.
# Cleaner Anna is cleaning hall number 5.
