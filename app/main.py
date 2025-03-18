from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


# # Bar test
# cb = CinemaBar()
# customer = Customer("Bob", "popcorn")
# cb.sell_product(customer=customer, product=customer.food)

# # Hall test
# hall = CinemaHall(hall_number=5)
# movie_name = "Madagascar"
# customers = [
#     Customer(name="Bob", food="Coca-cola"),
#     Customer(name="Alex", food="popcorn")
# ]
# cleaning_staff = Cleaner(name="Anna")
#
# hall.movie_session(movie_name=movie_name,
# customers=customers, cleaning_staff=cleaning_staff)
#
# anna = Cleaner(name="Anna")
# anna.clean_hall(hall_number=5)

def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_objects = []
    for customer_data in customers:
        customer_objects.append(Customer(name=customer_data["name"],
                                         food=customer_data["food"]))
    for customer in customer_objects:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaning_staff)

#
# customers = [
#     {"name": "Bob", "food": "Coca-cola"},
#     {"name": "Alex", "food": "popcorn"}
# ]
# hall_number = 5
# cleaner_name = "Anna"
# movie = "Madagascar"
#
# cinema_visit(customers=customers, hall_number=hall_number,
# cleaner=cleaner_name, movie=movie)
#
