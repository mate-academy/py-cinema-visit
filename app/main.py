from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(movie, customers, hall_number, cleaner):
    customer_objects = []

    for customer in customers:
        customer_obj = Customer(
            name=customer["name"],
            food=customer["food"]
        )
        customer_objects.append(customer_obj)

        CinemaBar.sell_product(
            product=customer_obj.food,
            customer=customer_obj
        )

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
