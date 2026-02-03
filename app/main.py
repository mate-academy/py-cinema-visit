from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar



def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str)-> None:
        customer_instances = []
        for person in customers:
            cust = Customer(name=person["name"], food=person["food"])
            customer_instances.append(cust)
            CinemaBar.sell_product(product=cust.food, customer=cust)

        cleaning_staff = Cleaner(name=cleaner)
        hall = CinemaHall(hall_number=hall_number)

        hall.movie_session(
            movie_name=movie,
            customers=customer_instances,
            cleaning_staff=cleaning_staff
        )