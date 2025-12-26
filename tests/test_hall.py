from app.cinema_hall import CinemaHall

def test_cinema_hall():
    hall = CinemaHall(1, 100)
    hall.start_session("Inception")
    hall.end_session("Inception")

