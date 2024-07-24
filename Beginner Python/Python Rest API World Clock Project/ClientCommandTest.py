# Jack Cacela and Spencer Marks
# Python World Clock API Project

# To run this code, download this file, ensuring it is in the same directory as Client.py and EndpointApp.py, and in the command prompt navigate to the appropriate directory.
# Once this is done, ensure that you already ran the EndpointApp.py file so port 8080 is listening for a GET request.
# Then, run this ClientCommandTest.py file in the command prompt by typing the following: python ClientCommandTest.py
# Once the file is running, it will return the result of testing the scenario where Client.py is run with a viable and non viable parameter, and also without a parameter. This test should work given that the WorldClockAPI is up and running.

import unittest
import subprocess

class TestCommandLineClient(unittest.TestCase):
    def test_successful_cli_request(self):
        # Run the command-line client with a specific argument
        result = subprocess.run(['python', 'client.py', 'est'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Check if the exit code is 0 (successful)
        self.assertEqual(result.returncode, 0)

        # Check if the output contains the expected string
        expected_string = "Current time in est:"
        self.assertIn(expected_string, result.stdout)


    def test_unsuccessful_cli_request1(self):
        # Run the command-line client with no arguments
        result = subprocess.run(['python', 'client.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Check if the exit code is 1 (indicating an error)
        self.assertEqual(result.returncode, 1)

        # Check if the error message matches the expected usage message
        expected_error_message = 'Usage: python client.py <timezone>\n'
        self.assertEqual(result.stderr, expected_error_message)

    def test_unsuccessful_cli_request2(self):
        # Run the command-line client with no arguments
        result = subprocess.run(['python', 'client.py', 'esta'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Check if the exit code is 1 (indicating an error)
        self.assertEqual(result.returncode, 1)

        # Check if the error message matches the expected usage message
        expected_error_message = 'Usage: python client.py <timezone>\n'
        self.assertEqual(result.stderr, expected_error_message)

if __name__ == '__main__':
    unittest.main()