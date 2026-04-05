from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cust_list = []

    for cust in customers:
        customer_instances = Customer(
            name=cust["name"],
            food=cust["food"]
        )

        CinemaBar.sell_product(
            product=customer_instances.food,
            customer=customer_instances
        )
        cust_list.append(customer_instances)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie_name=movie,
                       customers=cust_list,
                       cleaning_staff=cleaning_staff)
