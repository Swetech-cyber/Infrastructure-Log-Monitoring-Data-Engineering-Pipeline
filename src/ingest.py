import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# PostgreSQL connection details
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Create PostgreSQL connection
DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=int(DB_PORT),
    database=DB_NAME
)

engine = create_engine(DATABASE_URL)

# Read CSV file
df = pd.read_csv("data/raw/infrastructure_logs.csv")

print(f"Loaded {len(df)} records from CSV.")

# Clear previous raw data
with engine.begin() as connection:
    connection.execute(
        text("TRUNCATE TABLE infrastructure_logs")
    )

print("Previous raw records cleared.")

# Load fresh data into PostgreSQL
df.to_sql(
    "infrastructure_logs",
    engine,
    if_exists="append",
    index=False
)

print("Raw data successfully loaded into PostgreSQL.")