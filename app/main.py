from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    list_of_customers = [Customer(name_n_food["name"],
                                  name_n_food["food"])
                         for name_n_food in customers]
    c_bar = CinemaBar()
    for customer in list_of_customers:
        c_bar.sell_product(customer.food, customer)
    cinema_instance = CinemaHall(hall_number)
    staff_instance = Cleaner(cleaner)
    cinema_instance.movie_session(movie,
                                  list_of_customers,
                                  staff_instance
                                  )
