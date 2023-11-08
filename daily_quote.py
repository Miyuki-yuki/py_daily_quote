import sys
import csv
from datetime import datetime, timedelta

def generate_daily_quotes(start_date, end_date, csv_file_path):
    date_format = "%Y-%m-%d"
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)
    delta = end - start

    # Read quotes from a CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        quotes = [row[0] for row in reader]  # Assuming each quote is in the first column

    for i in range(delta.days + 1):
        date = start + timedelta(days=i)
        quote = quotes[i % len(quotes)]
        print(f"Quote for {date.strftime(date_format)}: {quote}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: daily_quote.py <start_date> <end_date> <csv_file_path>")
        sys.exit(1)

    start_date = sys.argv[1]
    end_date = sys.argv[2]
    csv_file_path = sys.argv[3]  # The path to the CSV file
    generate_daily_quotes(start_date, end_date, csv_file_path)
