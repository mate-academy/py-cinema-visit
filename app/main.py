from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: int,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customer_list = []
    for customer in customers:
        customer_list.append(Customer(
            name=customer["name"],
            food=customer["food"])
        )
    for customer in customer_list:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )
    cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customer_list, cleaner)
