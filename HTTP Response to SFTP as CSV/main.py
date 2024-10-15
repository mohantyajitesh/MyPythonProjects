from api_client import fetch_api_data
from data_transformer import convert_json_to_csv
from sftp_client import upload_csv_to_sftp

def main():
    
    sftp_host = "hostname"  # Replace with your SFTP server details
    sftp_port = "port"
    sftp_username = "username"
    sftp_password = "password"
    sftp_remote_path = "remote_path"

    try:
        # Fetch JSON data from API
        json_data = fetch_api_data()

        # Convert JSON data to CSV
        csv_data = convert_json_to_csv(json_data)

        # Upload CSV to SFTP
        upload_csv_to_sftp(csv_data, sftp_host, sftp_port, sftp_username, sftp_password, sftp_remote_path)

    except Exception as e:
        print(f"An error occurred during the process: {e}")

if __name__ == "__main__":
    main()