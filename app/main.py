from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers, hall_number, cleaner, movie):
    customers_instances = []
    for c in customers:
        customers_instances.append(Customer(name=c["name"], food=c["food"]))

    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)

    for customer in customers_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(
        movie_name=movie,
        customers=customers_instances,
        cleaning_staff=cleaning_staff
    )
