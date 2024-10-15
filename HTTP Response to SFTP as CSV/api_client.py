import requests
import configparser

global response_data 

def fetch_api_data():

  global response_data
  response_data_object = {}

  try:
    # Send a GET request to the API URL
    response = requests.get(api_url, auth=(username, password))

    # Raise an exception for error status codes
    response.raise_for_status()

    # Parse the JSON response
    response_data_object = response.json()
    response_data = response_data_object['items']
    return response_data

  except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")

#End of function definition

# Load configuration from a file named "config.ini"
config = configparser.ConfigParser()
config.read('config.ini')

# Retrieve details from the configuration file
api_url = config.get('api', 'api_url')
username = config.get('api', 'username')
password = config.get('api', 'password')

#Begin calling the function
fetch_api_data()

print(response_data)