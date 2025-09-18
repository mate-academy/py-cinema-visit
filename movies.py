from typing import Dict, Optional, Tuple

MOVIES: Dict[str, int] = {
    'Dune 2': 45,
    'Oppenheimer': 30,
    'Barbie': 25,
    'Inside Out 2': 35,
}


def list_movies() -> str:
    """Retorna uma lista formatada de filmes e preços."""
    return '\n'.join([f'{i + 1}. {m} - {p} NIS'for i,
                     (m, p) in enumerate(MOVIES .items())])


def get_movie_price(movie: str) -> Optional[int]:
    """Preço de um filme pelo nome (ou None se inválido)."""
    return MOVIES .get(movie)


def get_movie_by_index(idx: int) -> Optional[Tuple[str, int]]:
    """Retorna (nome, preço) do filme pelo índice 1-based; None se inválido."""
    if 1 <= idx <= len(MOVIES):
        name = list(MOVIES .keys())[idx - 1]
        return name, MOVIES[name]
    return None
