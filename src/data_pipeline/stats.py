from __future__ import annotations
from dataclasses import dataclass
import numpy as np
import pandas as pd


@dataclass
class StatsResult:
    media_preco: float
    desvio_preco: float
    receita_total: float
    top_categoria: str


def compute_stats(df: pd.DataFrame) -> StatsResult:
    preco = df["preco"].to_numpy(dtype=float)
    quantidade = df["quantidade"].to_numpy(dtype=int)
    receita = preco * quantidade
    media = float(np.mean(preco))
    desvio = float(np.std(preco, ddof=1)) if len(preco) > 1 else 0.0
    total = float(np.sum(receita))
    top_categoria = (
        df.groupby("categoria")["quantidade"].sum().sort_values(ascending=False).index[0]
    )
    return StatsResult(media, desvio, total, top_categoria)
