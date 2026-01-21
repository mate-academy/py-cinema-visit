from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    my_customers = []
    my_hall = CinemaHall(hall_number)
    my_cleaner = Cleaner(cleaner)

    for customer_info in customers:
        customer = Customer(name=customer_info["name"],
                            food=customer_info["food"])
        my_customers.append(customer)
        CinemaBar.sell_product(customer=customer, product=customer.food)

    my_hall.movie_session(movie_name=movie,
                          customers=my_customers,
                          cleaning_staff=my_cleaner)
