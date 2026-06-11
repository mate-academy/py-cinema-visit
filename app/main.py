from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str
) -> None:
    list_of_customers = []
    for customer in customers:
        new_customer = Customer(name=customer["name"], food=customer["food"])
        list_of_customers.append(new_customer)
        CinemaBar.sell_product(
            customer=new_customer,
            product=new_customer.food
        )
    hall = CinemaHall(hall_number)
    today_cleaner = Cleaner(cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=today_cleaner
    )
