import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

import app.cinema.bar
import app.cinema.hall
import app.people.customer
import app.people.cinema_staff
import app.main

def test_imports():
    assert True  # Só para garantir que os imports não causam erro

