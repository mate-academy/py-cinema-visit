from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_obj = []

    for customer in customers:
        new_customer = Customer(name=customer["name"], food=customer["food"])
        customer_obj.append(new_customer)
        CinemaBar.sell_product(product=new_customer.food,
                               customer=new_customer)

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_obj,
        cleaning_staff=cleaning_staff)
