from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    movie: str,
    customers: list,
    hall_number: int,
    cleaner: str,
) -> None:

    if isinstance(movie, list):
        old_customers = movie
        old_hall_number = customers
        old_cleaner = hall_number
        old_movie = cleaner
        movie = old_movie
        customers = old_customers
        hall_number = old_hall_number
        cleaner = old_cleaner


    customers_in = customers
    created_customers = []
    for customer_in in customers_in:
        new_customer = Customer(
            name=customer_in["name"], food=customer_in["food"]
        )
        CinemaBar.sell_product(
            product=customer_in["food"], customer=new_customer
        )
        created_customers.append(new_customer)
    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=created_customers,
        cleaning_staff=cleaner_obj
    )
