from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customer_instance = [Customer(name=cust["name"],
                                  food=cust["food"])
                         for cust in customers]
    cleaner_instance = Cleaner(name=cleaner)

    for customer in customer_instance:
        CinemaBar.sell_product(product=customer.food,
                               customer=customer)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie_name=movie,
                       customers=customer_instance,
                       cleaning_staff=cleaner_instance)

#
# customers = [
#     {"name": "Bob", "food": "Coca-cola"},
#     {"name": "Alex", "food": "popcorn"}
# ]
# hall_number = 5
# cleaner_name = "Anna"
# movie = "Madagascar"
#
# cinema_visit(customers=customers,
# hall_number=number,
# cleaner=cleaner_name,
# movie_arg=movie)
