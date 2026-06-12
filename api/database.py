from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql://postgres:postgres@localhost:5432/skyprice_ai"
)

engine = create_engine(DATABASE_URL)