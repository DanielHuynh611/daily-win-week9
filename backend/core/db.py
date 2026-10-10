"""SQLAlchemy Core storage shared by every generated feature."""
import click
from flask import current_app
from sqlalchemy import (
    CheckConstraint, Column, Date, DateTime, ForeignKey, MetaData, String,
    Table, UniqueConstraint, create_engine, event,
)
from sqlalchemy.pool import StaticPool

metadata = MetaData()
users = Table(
    "users", metadata,
    Column("id", String(36), primary_key=True),
    Column("email", String(254), nullable=False, unique=True),
    Column("password_hash", String(255), nullable=False),
    Column("created_at", DateTime, nullable=False),
)
wins = Table(
    "f_99d93461__wins", metadata,
    Column("id", String(36), primary_key=True),
    Column("user_id", String(36), ForeignKey("users.id"), nullable=False),
    Column("date", Date, nullable=False),
    Column("achievement_text", String(150), nullable=False),
    Column("timezone", String(64), nullable=False),
    Column("created_at", DateTime, nullable=False),
    UniqueConstraint("user_id", "date", name="uq_win_user_date"),
    CheckConstraint("length(trim(achievement_text)) BETWEEN 1 AND 150", name="ck_win_text"),
)


def configure_database(app):
    url = app.config["DATABASE_URL"]
    options = {"pool_pre_ping": True}
    if url.startswith("sqlite"):
        options["connect_args"] = {"check_same_thread": False}
        if ":memory:" in url:
            options["poolclass"] = StaticPool
    else:
        options.update(pool_size=3, max_overflow=2, pool_recycle=1800)
    engine = create_engine(url, **options)
    if engine.dialect.name == "sqlite":
        @event.listens_for(engine, "connect")
        def sqlite_foreign_keys(connection, _record):
            connection.execute("PRAGMA foreign_keys=ON")
    elif engine.dialect.name == "mysql":
        @event.listens_for(engine, "connect")
        def mysql_utc(connection, _record):
            cursor = connection.cursor()
            cursor.execute("SET time_zone = '+00:00'")
            cursor.close()
    app.extensions["database_engine"] = engine
    if app.testing:
        metadata.create_all(engine)

    @app.cli.command("init-db")
    def init_db():
        """Create missing tables; existing records are preserved."""
        metadata.create_all(engine)
        click.echo("Daily Win database tables are ready.")


def get_engine():
    return current_app.extensions["database_engine"]
