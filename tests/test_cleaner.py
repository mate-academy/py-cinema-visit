import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app.people.cinema_staff import Cleaner

def test_clean_hall(capsys):
    cleaner = Cleaner(name="Anna")
    cleaner.clean_hall(hall_number=5)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Cleaner Anna is cleaning hall number 5."
