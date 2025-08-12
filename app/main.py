from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers, number, cleaner, movie):
    customer_objects = []

    for customer_data in customers:
        customer = Customer(name = customer_data['name'], food = customer_data['food'])
        CinemaBar.sell_product(product = customer.food, customer = customer)
        customer_objects.append(customer)

    cleaning_staff = Cleaner(name = cleaner)
    hall_number = CinemaHall(number = number)
    hall_number.movie_session(movie_name = movie,
                              customers = customer_objects,
                              cleaning_staff = cleaning_staff
)
