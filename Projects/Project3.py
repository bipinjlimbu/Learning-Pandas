import pandas as pd
from Project2 import df
from datetime import datetime

# Feature Extraction: Calculating the total number of months from the 'Timestamp' column

def calculate_months(timestamp):
    try:
        start_str, end_str = timestamp.split(' - ')

        # Convert start date
        start_date = datetime.strptime(start_str.strip(), "%b %Y")

        # Handle "Present"
        if "Present" in end_str:
            end_date = datetime.today()
        else:
            end_date = datetime.strptime(end_str.strip(), "%b %Y")

        # Calculate months difference
        total_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

        return total_months

    except:
        return None


df['Months'] = df['Timestamp'].apply(calculate_months)

if __name__ == "__main__":
    print("\nFirst 5 rows with Total Months:\n")
    print(df.head())