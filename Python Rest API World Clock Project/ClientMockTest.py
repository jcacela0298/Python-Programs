# Jack Cacela and Spencer Marks
# Python World Clock API Project

# To run this code, download this file and in the command prompt navigate to the appropriate directory.
# Once this is done, ensure that you already ran the EndpointApp.py file so port 8080 is listening for a GET request.
# Then, run this ClientMockTest.py file in the command prompt by typing the following: python ClientMockTest.py
# Once the file is running, it will return the result of testing a positive status code (200) and an error code (404) given that the WorldClockAPI is up and running.

import unittest
from unittest.mock import patch
import requests
from Client import get_current_time

class TestClient(unittest.TestCase):
    @patch('requests.get')
    def test_successful_request(self, mock_get):
        # Mock the response from the server
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response.json = lambda: {"time": "2023-10-27T15:30:00Z"}
        mock_get.return_value = mock_response

        # Call the function being tested
        result = get_current_time("est")

        # Check if the function returns the expected output
        expected_output = "Current time in est: 2023-10-27T15:30:00Z"
        self.assertEqual(result, expected_output)

    @patch('requests.get')
    def test_failed_request(self, mock_get):
        # Mock a failed response from the server
        mock_response = requests.Response()
        mock_response.status_code = 404
        mock_response.json = lambda: {"error": "Time not available"}
        mock_get.return_value = mock_response

        # Call the function being tested
        result = get_current_time("est")

        # Check if the function returns the expected output
        expected_output = 'Failed to fetch time from the endpoint. Status code: 404'
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()