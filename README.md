# SQLite to CSV Converter

This Python program is designed to convert SQLite database tables into CSV files. It is particularly useful when you need to extract data from a SQLite database and import it into a different application.

## Requirements

- Python 3.x
- `sqlite3` module
- `csv` module

## Installation

1. Clone this repository or download the `sqlite_to_csv_converter.py` file.
2. Install the required modules using pip: `pip install sqlite3 csv`

## Usage

1. Place your SQLite database file(s) in the `source` directory.
2. Run the `sqlite_to_csv_converter.py` program in your Python environment.
3. The program will automatically create a new directory called `result` to store the CSV files. If the `result` directory already exists, the program will remove all files in the directory before proceeding.
4. The program will loop through all SQLite files in the `source` directory (excluding `.gitignore` and `.gitkeep` files), extract all tables from each database, and save them as separate CSV files in a folder with the same name as the original database file.

## Troubleshooting

- If you encounter a `sqlite3.DatabaseError: file is not a database` error, it is likely that the file you are attempting to convert is not a SQLite database. Make sure that the file has a `.sqlite` or `.db` extension.
- If you encounter a `FileNotFoundError`, make sure that the `source` directory contains the correct files and that they are named and formatted correctly.
- If you encounter any other issues, please create an issue in the GitHub repository.

