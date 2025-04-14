class CinemaHall:
    def __init__(self, hall_id, capacity):
        self.hall_id = hall_id
        self.capacity = capacity

    def start_session(self, movie):
        print(f"{movie} started in hall number {self.hall_id}.")

    def end_session(self, movie):
        print(f"{movie} ended in hall number {self.hall_id}.")