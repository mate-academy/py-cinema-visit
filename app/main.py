from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str, movie: str) -> None:

    customer_list = []
    for customer in customers:
        new_customer_instance = Customer(customer["name"], customer["food"])
        customer_list.append(new_customer_instance)

        CinemaBar.sell_product(product=new_customer_instance.food,
                               customer=new_customer_instance)

    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(cleaner)
    hall.movie_session(movie_name=movie, customers=customer_list,
                       cleaning_staff=cleaner_instance)
