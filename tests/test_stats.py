from src.data_pipeline.stats import compute_stats
import pandas as pd


def test_compute_stats_basic():
    df = pd.DataFrame(
        {
            "preco": [10.0, 20.0, 30.0],
            "quantidade": [1, 2, 3],
            "categoria": ["A", "A", "B"],
            "produto": ["p1", "p2", "p3"],
            "canal": ["online", "online", "loja"],
        }
    )
    stats = compute_stats(df)
    assert stats.media_preco == 20.0
    assert stats.top_categoria == "A"
