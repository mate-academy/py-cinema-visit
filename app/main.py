from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) \
        -> None:
    list_of_customers = [Customer(name=customer_data["name"],
                                  food=customer_data["food"])
                         for customer_data in customers]
    for customer in list_of_customers:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    hall.movie_session(movie_name=movie, customers=list_of_customers,
                       cleaning_staff=cleaner_obj)
