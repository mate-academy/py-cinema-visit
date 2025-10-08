class CinemaHall(object):
    def __init__(self, hall_number):
        self.hall_number = hall_number

    def start_movie(self, movie_name, customers, cleaning_staff):
        customer_names = ", ".join(customers)
        staff_names = ", ".join([staff.name for staff in cleaning_staff])
        return (
            "Starting '{}' in hall {}.\n"
            "Customers: {}\n"
            "Cleaning staff: {}".format(
                movie_name, self.hall_number, customer_names, staff_names
            )
        )
