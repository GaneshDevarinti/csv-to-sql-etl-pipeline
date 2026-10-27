
import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent / "sales.db"

with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()

    # Check total records
    cursor.execute("SELECT COUNT(*) FROM sales")
    total_records = cursor.fetchone()[0]
    print("Total records:", total_records)

    # Check total revenue
    cursor.execute("SELECT SUM(revenue) FROM sales")
    total_revenue = cursor.fetchone()[0]
    print("Total revenue:", total_revenue)

    # View all cleaned records
    cursor.execute("SELECT * FROM sales")
    for row in cursor.fetchall():
        print(row)
