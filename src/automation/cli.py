from __future__ import annotations
import argparse
from pathlib import Path
from json import dumps
from datetime import datetime

from src.config import settings
from src.automation.logging_config import configure_logging
from src.data_pipeline.ingest import init_db, seed_if_empty
from src.data_pipeline.transform import load_dataframe, ensure_dirs
from src.data_pipeline.stats import compute_stats
from src.models_inference.inference import generate_insight


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Pipeline de dados + insight IA")
    p.add_argument("--db", default=settings.db_path)
    p.add_argument("--model", default=settings.model_name)
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--outdir", default="outputs")
    return p


def main() -> None:
    logger = configure_logging(settings.log_level)
    parser = build_parser()
    args = parser.parse_args()

    logger.info("Inicializando banco")
    init_db(args.db)
    inserted = seed_if_empty(args.db)
    if inserted:
        logger.info("%d linhas inseridas", inserted)

    df = load_dataframe(args.db)
    if args.limit:
        df = df.head(args.limit)

    stats = compute_stats(df)
    logger.info("Métricas calculadas: %s", stats)

    insight = generate_insight(stats, model_name=args.model)
    logger.info("Insight gerado")

    ensure_dirs(Path(args.outdir))
    output = {
        "timestamp": datetime.utcnow().isoformat(),
        "model": args.model,
        "stats": stats.__dict__,
        "insight": insight,
    }
    out_path = Path(args.outdir) / "insight.json"
    out_path.write_text(dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    logger.info("Arquivo salvo em %s", out_path)


if __name__ == "__main__":  # pragma: no cover
    main()
