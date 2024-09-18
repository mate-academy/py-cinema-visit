from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customer_list: list,
        hall_num: int,
        cleaner_person: str,
        movie_title: str
) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_num)
    cleaning_staff = Cleaner(cleaner_person)

    customer_objects = []
    for customer_data in customer_list:
        customer = Customer(customer_data["name"], customer_data["food"])
        cinema_bar.sell_product(product=customer.food, customer=customer)
        customer_objects.append(customer)

    hall.movie_session(movie_name=movie_title,
                       customers=customer_objects,
                       cleaning_staff=cleaning_staff)
