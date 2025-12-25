import builtins
from typing import Optional
import pytest

from utils import print_line, ask_int


def test_print_line_default(capsys):
    print_line()  # width padrão = 40
    captured = capsys.readouterr()
    assert captured.out == "-" * 40 + "\n"


def test_print_line_custom_width(capsys):
    print_line(10)
    captured = capsys.readouterr()
    assert captured.out == "-" * 10 + "\n"


def test_ask_int_valid(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "42")
    assert ask_int("n? ") == 42


def test_ask_int_invalid(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "abc")
    assert ask_int("n? ") is None


def test_ask_int_negative(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "-5")
    assert ask_int("n? ") == -5


def test_ask_int_with_spaces(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "   7  ")
    assert ask_int("n? ") == 7
