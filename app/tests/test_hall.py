from ..cinema.hall import CinemaHall

def test_cinema_hall_constructor():
    ch = CinemaHall(hall_number=6)  # Changed from number=6 to hall_number=6
    assert ch.hall_number == 6