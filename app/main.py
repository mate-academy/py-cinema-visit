from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[Customer], hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_list = []
    for customer in customers:
        customer_obj = Customer(name=customer["name"],
                                food=customer["food"])
        customers_list.append(customer_obj)
        CinemaBar.sell_product(product=customer_obj.food,
                               customer=customer_obj)
    cinema_hall = CinemaHall(number=hall_number)
    hall_cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie_name=movie, customers=customers_list,
                              cleaning_staff=hall_cleaner)
