from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_new = []
    for customer in customers:
        name = customer.get("name")
        food = customer.get("food")
        customers_new.append(Customer(name, food))
        CinemaBar.sell_product(customer=Customer(name, food),
                               product=food)

    cleaner = Cleaner(cleaner)

    cinema_hall_instance = CinemaHall(hall_number)
    # customers_new = []
    # for human in customers:
    #     customers_new.append(Customer(human.get("name"), human.get("food")))
    cinema_hall_instance.movie_session(cleaning_staff=cleaner,
                                       customers=customers_new,
                                       movie_name=movie)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers,
             hall_number=5,
             cleaner="Anna",
             movie="Madagascar")
