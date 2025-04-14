from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    # make the list of instances from making instances in file customer.py
    list_of_viewers = [Customer(person.get("name"), person.get("food"))
                       for person in customers]

    # create instances for bar and hall
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)

    # buying food from each instance in Customer
    for viewer in list_of_viewers:
        cinema_bar.sell_product(viewer.food, viewer)

    # create instance of Cleaner in file cinema_staff.py
    cleaner_today = Cleaner(cleaner)

    # run the function which print start of movie, viewers and end of movie
    cinema_hall.movie_session(movie, list_of_viewers, cleaner_today)
