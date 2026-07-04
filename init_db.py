from sqlalchemy import text

from database import engine
from models import Base


def init_db() -> None:
    print("Connecting to PostgreSQL and enabling extensions...")
    with engine.begin() as connection:
        # This is vital for generating your UUID primary keys safely!
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS pgcrypto"))

    print("Creating your 10 startup memory tables...")
    Base.metadata.create_all(engine)
    print("🎉 Database tables initialized successfully.")

if __name__ == "__main__":
    init_db()
