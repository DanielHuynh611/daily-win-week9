"""Load the same environment variables used by the Zorentia EC2 workflow."""
import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Settings:
    database_url: str
    jwt_secret: str
    jwt_issuer: str


def get_settings(testing=False):
    load_dotenv(PROJECT_ROOT / ".env", override=False)
    database_url = os.getenv("DATABASE_URL", "").strip()
    jwt_secret = os.getenv("JWT_SECRET", "").strip()
    if testing:
        database_url = "sqlite+pysqlite:///:memory:"
        jwt_secret = "test-only-secret-not-for-deployment"
    if not database_url:
        raise RuntimeError("DATABASE_URL is required. Configure the project .env file.")
    if not jwt_secret or (not testing and (len(jwt_secret) < 32 or jwt_secret.startswith("replace-"))):
        raise RuntimeError("JWT_SECRET must be a random value of at least 32 characters.")
    return Settings(database_url, jwt_secret, os.getenv("JWT_ISSUER", "zorentia-app"))
