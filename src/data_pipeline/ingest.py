from __future__ import annotations
import sqlite3
from pathlib import Path
from typing import Sequence

from .transform import ensure_dirs

SEED_DATA = [
    ("Notebook Gamer", "Eletronicos", 8500.0, 5, "online"),
    ("Mouse Óptico", "Perifericos", 80.0, 120, "loja"),
    ("Teclado Mecânico", "Perifericos", 450.0, 40, "online"),
    ("Monitor 4K", "Eletronicos", 2100.0, 15, "loja"),
    ("Headset", "Perifericos", 320.0, 60, "online"),
]

DDL = """
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    categoria TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL,
    canal TEXT NOT NULL
);
"""

INSERT = "INSERT INTO vendas (produto, categoria, preco, quantidade, canal) VALUES (?, ?, ?, ?, ?)"  # noqa: E501


def init_db(db_path: str) -> None:
    ensure_dirs(Path(db_path).parent)
    with sqlite3.connect(db_path) as conn:
        conn.execute(DDL)
        conn.commit()


def seed_if_empty(db_path: str, rows: Sequence[tuple] | None = None) -> int:
    rows = rows or SEED_DATA
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM vendas")
        (count,) = cur.fetchone()
        if count == 0:
            cur.executemany(INSERT, rows)
            conn.commit()
            return len(rows)
        return 0
