from __future__ import annotations
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    db_path: str = os.getenv("DB_PATH", "data/demo.db")
    model_name: str = os.getenv("MODEL_NAME", "distilgpt2")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()
