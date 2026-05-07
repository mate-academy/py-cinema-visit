from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = [Customer(cust["name"],
                              cust["food"]) for cust in customers]
    for customer in customer_list:
        CinemaBar.sell_product(product=customer.food,
                               customer=customer)
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie_name=movie,
                       customers=customer_list,
                       cleaning_staff=cleaning_staff)
