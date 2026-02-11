from app.cinema.bar import CinemaBar
import app.people.customer.Customer
import app.cinema.hall.CinemaHall
import app.people.cinema_staff.Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    custs = []
    for cust in customers:
        custs.append(Customer(cust["name"], cust["food"]))
    cleaner1 = Cleaner(cleaner)
    cinemahall1 = CinemaHall(hall_number)
    cinemahall1.movie_session(movie, custs, cleaner1)
