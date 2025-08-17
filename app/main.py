from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer

def cinema_visit(movie, customers, hall_number, cleaner):
    # Create hall and cleaner objects
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    # Create Customer objects
    customer_list = [Customer(customer["name"], customer["food"]) for customer in customers]

    # Sell products to customers
    for customer in customer_list:
        CinemaBar.sell_product(customer.food, customer)

    # Start the movie session
    cinema_hall.movie_session(movie, customer_list, cleaning_staff)
