from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers_list: list,
                 hall_number_visit: int,
                 cleaner: str,
                 movie_arg: str
                 ) -> None:
    customer_instance = [Customer(name=cust["name"],
                                  food=cust["food"])
                         for cust in customers_list]
    cleaner_instance = Cleaner(name=cleaner)

    for customer in customer_instance:
        CinemaBar.sell_product(product=customer.food,
                               customer=customer)

    hall = CinemaHall(hall_number_visit)
    hall.movie_session(movie_name=movie_arg,
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
# cinema_visit(customers_list=customers,
# hall_number_visit=hall_number,
# cleaner=cleaner_name,
# movie_arg=movie)
