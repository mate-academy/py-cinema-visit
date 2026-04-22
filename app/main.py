from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    # write you code here
    cleaner_obj = Cleaner(name=cleaner)
    hall_obj = CinemaHall(number=hall_number)
    customers_obj = []
    for cus in customers:
        new_customer = Customer(name=cus["name"], food=cus["food"])
        customers_obj.append(new_customer)
        CinemaBar.sell_product(
            product=new_customer.food,
            customer=new_customer
        )

    hall_obj.movie_session(
        movie_name=movie,
        customers=customers_obj,
        cleaning_staff=cleaner_obj
    )
