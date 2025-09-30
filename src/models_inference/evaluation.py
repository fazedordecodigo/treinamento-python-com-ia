from __future__ import annotations
import re


def repetition_score(text: str, n: int = 3) -> float:
    """Retorna proporção de n-gramas repetidos (simplificado)."""
    tokens = text.split()
    if len(tokens) < n * 2:
        return 0.0
    seen = set()
    repeated = 0
    for i in range(len(tokens) - n + 1):
        gram = tuple(tokens[i : i + n])
        if gram in seen:
            repeated += 1
        else:
            seen.add(gram)
    total = max(len(tokens) - n + 1, 1)
    return repeated / total


def contains_kpis(text: str) -> bool:
    patterns = [r"preço", r"receita", r"categoria"]
    return any(re.search(p, text.lower()) for p in patterns)
