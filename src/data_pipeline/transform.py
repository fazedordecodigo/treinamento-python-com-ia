from __future__ import annotations
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text


def ensure_dirs(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def load_dataframe(db_path: str) -> pd.DataFrame:
    engine = create_engine(f"sqlite:///{db_path}")
    with engine.connect() as conn:
        df = pd.read_sql(text("SELECT * FROM vendas"), conn)
    return df
