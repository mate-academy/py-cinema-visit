from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:

    customers_list = []
    for cust in customers:
        customer = Customer(name=cust["name"], food=cust["food"])
        customers_list.append(customer)

    for customer in customers_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)

    hall.movie_session(movie_name=movie,
                       customers=customers_list,
                       cleaning_staff=cleaning_staff)
