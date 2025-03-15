from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie_name: str
) -> None:
    list_of_customers = []
    cleaner_instance = Cleaner(cleaner)
    cinema_instance = CinemaHall(hall_number)
    bar_instance = CinemaBar()
    for customer_of_the_cinema_hall in customers:
        list_of_customers.append(Customer(customer_of_the_cinema_hall["name"],
                                          customer_of_the_cinema_hall["food"]))
    for customer in list_of_customers:
        bar_instance.sell_product(customer,
                                  customer.food)
    cinema_instance.movie_session(movie_name,
                                  list_of_customers, cleaner_instance)
