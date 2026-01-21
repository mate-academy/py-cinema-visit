from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

# write your imports here


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    # write you code here
    cleaner_inst = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    customers_list = []
    for customer in customers:
        customers_list.append(Customer(
            name=customer["name"],
            food=customer["food"]))
        CinemaBar.sell_product(
            customer=customer["name"],
            product=customer["food"])
    cinema_hall.movie_session(movie, customers_list, cleaner_inst)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers,
             hall_number=5, cleaner="Anna",
             movie="Madagascar")
