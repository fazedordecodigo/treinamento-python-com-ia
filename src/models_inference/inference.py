from __future__ import annotations
try:
    from transformers import pipeline
except ImportError:  # pragma: no cover
    pipeline = None  # type: ignore

from src.data_pipeline.stats import StatsResult


def generate_insight(stats: StatsResult, model_name: str = "distilgpt2") -> str:
    if pipeline is None:
        return "Transformers não instalado."

    prompt = (
        "Gere um insight de negócios em português considerando:\n"
        f"Preço médio: {stats.media_preco:.2f}; "
        f"Desvio: {stats.desvio_preco:.2f}; "
        f"Receita total: {stats.receita_total:.2f}; "
        f"Categoria top: {stats.top_categoria}.\nInsight:"
    )

    generator = pipeline("text-generation", model=model_name)
    out = generator(prompt, max_new_tokens=40, temperature=0.9, top_p=0.95)[0][
        "generated_text"
    ]
    return out.split("Insight:", 1)[-1].strip()
