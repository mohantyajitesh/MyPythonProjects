import pandas as pd
import json

def convert_json_to_csv_pandas(json_data: List[Dict]) -> str:

    try:
        # Load the JSON data
        data = json.loads(json_data)

        # Create a DataFrame from the JSON data
        df = pd.DataFrame(data)

        # Create a string buffer to hold the CSV data
        csv_buffer = io.StringIO()

        # Convert the DataFrame to CSV format and write it to the buffer
        df.to_csv(csv_buffer, index=False)

        # Get the string from the buffer
        csv_data = csv_buffer.getvalue()

        # Close the buffer
        csv_buffer.close()

        return csv_data

    except Exception as e:
        print(f"Failed to convert JSON to CSV: {e}")
        raise