
# CSV-to-SQL ETL Pipeline

## Overview
A beginner data engineering project that extracts sales
records from a CSV file, cleans and transforms them using
Python and Pandas, and loads them into a SQLite database.

## Architecture
CSV file -> Extract -> Transform -> Load -> SQLite -> SQL validation

## Technologies
- Python
- Pandas
- SQLite
- SQL
- Git and GitHub

## ETL Workflow
1. Read raw sales data from a CSV file.
2. Remove repeated order IDs.
3. Convert numeric columns to numeric data types.
4. Remove records with missing required fields.
5. Filter invalid quantities and prices.
6. Calculate revenue.
7. Load the cleaned records into the sales table.
8. Validate the record count and total revenue using SQL.

## How to Run

1. Install Python.
2. Install Pandas: `python -m pip install pandas`
3. Run: `python etl_pipeline.py`
4. Validate: `python validate.py`

## Sample Results
- Raw records: 6
- Cleaned records: 3
- Total revenue: 63000

## Limitations
This is a small batch-processing demonstration using
sample data and SQLite. It is not a production pipeline.
