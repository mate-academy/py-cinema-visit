import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app.people.customer import Customer

def test_watch_movie(capsys):
    customer = Customer(name="Bob", food="popcorn")
    customer.watch_movie(movie="Madagascar")
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Bob is watching "Madagascar".'
