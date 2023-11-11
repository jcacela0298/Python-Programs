# Jack Cacela and Spencer Marks
# Python World Clock API Project

# To run this code, download this file and in the command prompt and navigate to the appropriate directory.
# Once this is done, ensure that you already ran the EndpointApp.py file from the same directory so that port 8080 is listening for a GET request.
# Then, run this Client.py file in the command prompt by typing the following: python Client.py <timezone>. An example is python Client.py est
# Once the file is running, it will return the time of the time zone that is in the current_timezone variable, into the command line, given that the WorldClockAPI is up and running.

import sys
import requests

def get_current_time(timezone):
    # Set the endpoint URL for the Flask application
    endpoint_url = "http://localhost:8080/get_time"

    # Add the "timezone" query parameter to the URL
    params = {"timezone": timezone}

    # Make a GET request to the endpoint
    response = requests.get(endpoint_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        try:
            time_data = response.json()
            current_time = time_data.get('time', 'Time not available')
            output = f"Current time in {timezone}: {current_time}"
            return output  # Return the output string
        except ValueError:
            error_message = "Error: Unexpected response format from the server"
            print(error_message, file=sys.stderr)
            return error_message
    else:
        error_message = f"Failed to fetch time from the endpoint. Status code: {response.status_code}"
        print(error_message, file=sys.stderr)
        return error_message

if __name__ == "__main__":
    if len(sys.argv) != 2 or len(sys.argv[1]) != 3:
        print("Usage: python client.py <timezone>", file=sys.stderr)
        sys.exit(1)
    else:
        current_timezone = sys.argv[1]
        result = get_current_time(current_timezone)
        print(result)  # This line prints the result when the script is run from the command line