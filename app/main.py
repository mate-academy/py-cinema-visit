from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = []
    for cust in customers:
        customer = Customer(name=cust["name"], food=cust["food"])
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )
        customer_list.append(customer)
    hall = CinemaHall(number=hall_number)
    staff = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=staff
    )
