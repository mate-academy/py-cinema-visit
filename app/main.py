# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_customers = []
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    hall_employee = Cleaner(name=cleaner)
    for customer_information in customers:
        new_customer = Customer(customer_information["name"],
                                customer_information["food"])
        list_customers.append(new_customer)
        cinema_bar.sell_product(customer=new_customer,
                                product=new_customer.food)
    cinema_hall.movie_session(movie_name=movie,
                              customers=list_customers,
                              cleaning_staff=hall_employee)
