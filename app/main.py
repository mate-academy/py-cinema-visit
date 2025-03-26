from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []
    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)
    for customer in customers:
        customer = Customer(name=customer["name"],
                            food=customer["food"])
        cinema_bar.sell_product(customer=customer,
                                product=customer.food)
        customers_list.append(customer)

    cinema_hall.movie_session(movie_name=movie,
                              custumers=customers_list,
                              cleaning_stuff=cleaner)
