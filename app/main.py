from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar

# In the module `main.py` you have to import all this classes. Classes
# should be imported by absolute path, that starts with 'app.' with
# keyword 'from'. Write a
# function `cinema_visit` that takes `movie`, `customers` - a list
# of customers, elements are dicts with 'name' and desired 'food' of a
# customer, `hall_number` - number of the hall in cinema,
# `cleaner` - name of the cleaner, that will clean the
# hall after movie session.

# This function should create instances of `Customer`,
# `CinemaHall`, and `Cleaner`.
# First, the cinema bar should sell food to customers.
# To do this, you can use the `CinemaBar`
# class without creating an instance. Then,
# the cinema hall should schedule a movie session,
# and finally, a cleaner should clean the cinema hall.
# We expect each class to work with the provided data,
# accepting parameters in the correct order and having the necessary methods.
# No additional checks or error handling are needed!


def cinema_visit(movie: str, customers: list[dict],
                 hall_number: int, cleaner_name: str) -> None:
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)
    customer_objects = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customer_objects.append(customer)

    for customer in customer_objects:
        CinemaBar.sell_product(customer)

    hall.movie_session(movie, customer_objects, cleaner)
