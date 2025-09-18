import re
from movies import MOVIES, list_movies, get_movie_price, get_movie_by_index

def test_list_movies_has_all_entries():
    out = list_movies().strip().splitlines()
    assert len(out) == len(MOVIES)
    assert re.match(r"^\d+\.\s.+\s-\s\d+\sNIS$", out[0])

def test_get_movie_price_valid():
    some_title = next(iter(MOVIES.keys()))
    assert get_movie_price(some_title) == MOVIES[some_title]

def test_get_movie_price_invalid():
    assert get_movie_price("Filme Inexistente") is None

def test_get_movie_by_index_valid():
    name0 = list(MOVIES.keys())[0]
    price0 = MOVIES[name0]
    assert get_movie_by_index(1) == (name0, price0)

def test_get_movie_by_index_invalid():
    assert get_movie_by_index(0) is None
    assert get_movie_by_index(999) is None
