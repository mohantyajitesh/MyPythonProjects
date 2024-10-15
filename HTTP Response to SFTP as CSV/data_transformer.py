import csv
import io
from typing import List, Dict

def convert_json_to_csv(json_data: List[Dict]) -> str:
    """
    Convert JSON data to CSV format and return it as a string.
    :param json_data: List of dictionaries containing JSON data.
    :return: CSV formatted string.
    """
    try:
        if not json_data:
            raise ValueError("Empty JSON data provided.")

        # Create an in-memory file object
        csv_output = io.StringIO()
        fieldnames = json_data[0].keys()

        # Write to CSV
        writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(json_data)

        # Get the CSV string
        csv_data = csv_output.getvalue()
        csv_output.close()
        print(csv_data)
        return csv_data
    except Exception as e:
        print(f"Failed to convert JSON to CSV: {e}")
        raise
