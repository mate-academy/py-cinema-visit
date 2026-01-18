# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_customers = []
    for customer in customers:
        list_customers.append(Customer(customer["name"], customer["food"]))
    hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    for customer_el in list_customers:
        CinemaBar.sell_product(customer=customer_el,
                               product=customer_el.food)
    hall.movie_session(movie_name=movie,
                       customers=list_customers,
                       cleaning_staff=cleaner_staff)
#
# customers = [
#     {"name": "Bob", "food": "Coca-cola"},
#     {"name": "Alex", "food": "popcorn"}
# ]
# hall_number = 5
# cleaner_name = "Anna"
# movie = "Madagascar"
# cinema_visit(customers=customers,
# hall_number=hall_number, cleaner=cleaner_name, movie=movie)
# # Cinema bar sold Coca-cola to Bob.
# # Cinema bar sold popcorn to Alex.
# # "Madagascar" started in hall number 5.
# # Bob is watching "Madagascar".
# # Alex is watching "Madagascar".
# # "Madagascar" ended.
# # Cleaner Anna is cleaning hall number 5.
