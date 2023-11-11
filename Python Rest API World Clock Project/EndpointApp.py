# Jack Cacela and Spencer Marks
# Python REST API World Clock Project

# To run this code, download this file and in the command prompt navigate to the appropriate directory.
# Once this is done, run the file and the endpoint will be running on port 8080. 
# Open your browser and type: localhost:8080/get_time?timezone=est
# If the WorldClockAPI website is up and running, you should receive the time and date according to the EST time zone.

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get_time', methods=['GET'])
def get_time():
    timezone = request.args.get('timezone', 'est')  # Default to 'est' if not provided (example if the client only enters the url as "localhost:8080/get_time")
    api_url = f"http://worldclockapi.com/api/json/{timezone}/now"

# Make a request to the external API.
    response = requests.get(api_url)

    if response.status_code == 200:
        try:
            time_data = response.json()
            current_time = time_data.get('currentDateTime', 'Error: Time not available')
        except ValueError:
            current_time = 'Error: Unexpected response from the external API'
    else:
        error_message = f"Failed to fetch time from the endpoint. Status code: {response.status_code}"
        current_time = {'error': error_message}

    return jsonify({'time': current_time})

if __name__ == '__main__':
    app.run(host='localhost', port=8080)