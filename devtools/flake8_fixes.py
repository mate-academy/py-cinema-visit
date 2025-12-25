from __future__ import annotations

import io
import os
import re
import tokenize
from pathlib import Path
from typing import Iterable


TARGETS = ['movies.py', 'snacks.py', 'utils.py']
MAX_LEN = 88


def iter_targets(root: Path) -> Iterable[Path]:
    for name in TARGETS:
        path = root / name
        if path.exists():
            yield path


def to_single_quotes(code: str) -> str:
    """
    Converte aspas duplas para simples usando tokenize, preservando docstrings
    com três aspas e strings que contêm aspas simples.
    """
    out = []
    tokens = list(tokenize.generate_tokens(io.StringIO(code).readline))
    for tok_type, tok_str, *_ in tokens:
        if tok_type == tokenize.STRING:
            # pula triple-quoted
            if tok_str.startswith(('"""', "'''")):
                out.append((tok_type, tok_str))
                continue
            # converte "..." para '...' se seguro
            if tok_str.startswith('"') and tok_str.endswith('"'):
                inner = tok_str[1:-1]
                if "'" not in inner:  # evita conflito de aspas
                    tok_str = "'" + inner + "'"
            out.append((tok_type, tok_str))
        else:
            out.append((tok_type, tok_str))
    return tokenize.untokenize(out)


def soft_wrap_long_lines(code: str, max_len: int = MAX_LEN) -> str:
    """
    Tenta quebrar linhas longas em vírgulas quando dentro de (), [] ou {}.
    Mantém semântica (usa continuação implícita em parênteses). Se não
    encontrar vírgulas adequadas, mantém a linha e você pode usar # noqa: E501.
    """
    new_lines = []
    for line in code.splitlines():
        if len(line) <= max_len:
            new_lines.append(line)
            continue

        if any(ch in line for ch in '([{'):
            parts = []
            current = ''
            depth = 0
            in_str = False
            str_q = ''
            for ch in line:
                if in_str:
                    current += ch
                    if ch == str_q:
                        in_str = False
                    continue

                if ch in ('"', "'"):
                    in_str = True
                    str_q = ch
                    current += ch
                    continue

                if ch in '([{':
                    depth += 1
                elif ch in ')]}':
                    depth = max(0, depth - 1)

                if ch == ',' and depth > 0 and len(current) > max_len:
                    parts.append(current.rstrip())
                    current = ''
                else:
                    current += ch

            if current:
                parts.append(current.rstrip())

            if parts and not any(len(p) > max_len for p in parts):
                base_indent = re.match(r'\s*', line).group(0)
                indent = base_indent + '    '
                wrapped = (parts[0].rstrip(),) + tuple(
                    indent + p.lstrip() for p in parts[1:]
                )
                new_lines.extend(wrapped)
                continue

        new_lines.append(line)

    return '\n'.join(new_lines) + '\n'


def process_file(path: Path) -> None:
    original = path.read_text(encoding='utf-8')
    converted = to_single_quotes(original)
    wrapped = soft_wrap_long_lines(converted, MAX_LEN)

    if wrapped != original:
        path.write_text(wrapped, encoding='utf-8')
        print(f'Fixed: {path}')
    else:
        print(f'No change: {path}')


def main() -> None:
    root = Path(os.getcwd())
    for path in iter_targets(root):
        process_file(path)


if __name__ == '__main__':
    main()
