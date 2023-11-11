# Jack Cacela and Spencer Marks
# Python World Clock API Project

# To run this code, download this file, ensuring it is in the same directory as Client.py, and in the command prompt navigate to the appropriate directory.
# Once this is done, ensure that you already ran the EndpointApp.py file so port 8080 is listening for a GET request.
# Then, before running this ClientLiveEndpointTest.py file in the command prompt, make sure that the time in the expected output variable in our "test_live_successful_client_request" method below is equal to the time that the endpoint should receive.
# For example, if the current time is 10:50 AM on 11/11/2023 in  EST (GMT-5), we would put the follogin in the expected output variable: "Current time in est: 2023-11-11T10:49-05:00\n"
# Once the file is running, it will return the result of testing the scenario where Client.py is run with a normal est parameter, given that the WorldClockAPI is up and running. 

import unittest
import subprocess

class TestClientLiveEndpoint(unittest.TestCase):

    def test_live_successful_client_request(self):
        # Run the command-line client with a specific argument
        result = subprocess.run(['python', 'Client.py', 'est'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Check if the exit code is 0 (successful)
        self.assertEqual(result.returncode, 0)

        # Check if the output matches the expected result
        expected_output = "Current time in est: 2023-11-11T10:53-05:00\n"
        self.assertEqual(result.stdout, expected_output)


if __name__ == '__main__':
    unittest.main()