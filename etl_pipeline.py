
import pandas as pd
import sqlite3
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# Get the folder containing this Python file
BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "raw_sales.csv"
DB_FILE = BASE_DIR / "sales.db"


def extract():
    """Read raw sales data from the CSV file."""
    logging.info("Starting extraction")

    df = pd.read_csv(CSV_FILE)

    logging.info(f"Extracted {len(df)} records")
    return df


def transform(df):
    """Clean the data and calculate revenue."""
    logging.info("Starting transformation")

    # Remove duplicate order IDs, keeping the first occurrence
    df = df.drop_duplicates(
        subset=["order_id"]
    ).copy()

    # Convert numeric columns into numeric data types
    df["order_id"] = pd.to_numeric(
        df["order_id"], errors="coerce"
    )
    df["quantity"] = pd.to_numeric(
        df["quantity"], errors="coerce"
    )
    df["price"] = pd.to_numeric(
        df["price"], errors="coerce"
    )

    # Remove records with missing essential fields
    df = df.dropna(
        subset=["order_id", "product", "quantity", "price"]
    ).copy()

    # Reject invalid quantities and prices
    df = df[
        (df["quantity"] > 0) &
        (df["price"] >= 0)
    ].copy()

    # Calculate revenue for each order
    df["revenue"] = df["quantity"] * df["price"]

    logging.info(f"Records after cleaning: {len(df)}")
    return df


def load(df):
    """Load cleaned records into the SQLite database."""
    logging.info("Loading data into SQLite")

    with sqlite3.connect(DB_FILE) as conn:
        df.to_sql(
            "sales",
            conn,
            if_exists="replace",
            index=False
        )

    logging.info("Data loaded successfully")


def main():
    raw_data = extract()
    clean_data = transform(raw_data)
    load(clean_data)

    logging.info("ETL pipeline completed")


if __name__ == "__main__":
    main()
