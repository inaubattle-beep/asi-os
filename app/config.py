import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    model_mode: str = os.getenv("MODEL_MODE", "mock")
    model_base_url: str = os.getenv("MODEL_BASE_URL", "http://host.docker.internal:8000/v1")
    model_name: str = os.getenv("MODEL_NAME", "local-model")
    model_api_key: str = os.getenv("MODEL_API_KEY", "")
    workspace: str = os.getenv("WORKSPACE", "/workspace")
    db_path: str = "/data/asi_os.sqlite3"
    max_steps: int = int(os.getenv("MAX_STEPS", "8"))
    shell_timeout: int = int(os.getenv("SHELL_TIMEOUT", "20"))

settings = Settings()
