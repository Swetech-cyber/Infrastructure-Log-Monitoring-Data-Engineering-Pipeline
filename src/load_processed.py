import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Database configuration
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


# Create PostgreSQL connection URL
DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=int(DB_PORT),
    database=DB_NAME
)


# Create database engine
engine = create_engine(DATABASE_URL)


# Processed CSV file path
FILE_PATH = "data/processed/infrastructure_logs_processed.csv"


# Read processed data
df = pd.read_csv(FILE_PATH)

print(f"Loaded {len(df)} processed records from CSV.")


# Clear previously loaded processed records
with engine.begin() as connection:
    connection.execute(
        text("TRUNCATE TABLE infrastructure_logs_processed")
    )

print("Previous processed records cleared.")


# Load processed data into PostgreSQL
df.to_sql(
    "infrastructure_logs_processed",
    engine,
    if_exists="append",
    index=False
)

print("Processed data successfully loaded into PostgreSQL.")