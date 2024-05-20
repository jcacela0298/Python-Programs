This project was completed by Jack Cacela and Spencer Marks. 

The purpose of this project is to learn about REST API by communicating with the World Clock API.

In the EndpointApp.py file, we initialize the Flask application and define the Get Endpoint so we can make communications between the file and the World Clock API.

In the Client.py file, we make it so we can make Get requests via the command prompt by providing a parameter when we run the file -- For example: python Client.py est

In the ClientCommandTest.py file, we create three testing scenarios -- a viable, non-viable, and absent parameter for the Client.py file.

In the ClientMockTest.py file, we create mock data and a mock call to the WorldClockAPI to make sure the Client.py file will handle successful and unsuccessful error codes.

In the ClientLiveEndpointTest.py file, we test to see if the actual call to the WorldClockAPI is equal to what we set in the expected output variable.

There are more specific details about each file written within the files themselves at the top. Below are my additional comments/what I learned / acknowledgments for each file:
*
*
*
*
			EndpointApp.py File

For the first file, EndpointApp.py, I learned many things. First, we need to import Flask, which is Python's "popular web framework" which gives us all the tools and libraries for this project following REST principles. We need to import Flask, along with the request, requests, and jsonify modules to handle requests, generate JSON responses and make HTTP requests to an external API. The following code: app = Flask(__name__) is a way to initialize the flask application and make it so if this code is run as the main program, name gets converted to main (see code at very bottom) and this allows the flask application to run. @app.route is used to define a route for a GET request (which is triggered when the "/get_time" endpoint in the client code or Client.py file is requested for, or when we type the url "localhost:8080/get_time?timezone=est"), which would then proceed to the get_time() method within this file. To clarify further, the primary endpoint is the route defined by @app.route('/get_time', methods=['GET']). So, when we access the URL http://localhost:8080/get_time using a web browser / client that sends an HTTP GET request, we are actually interacting with the "get_time" endpoint. As we define the get_time() method, we set the required timezone parameter into the timezone variable, which is either what the user manually inputs in the url, or is est if the user only enters the url as "localhost:8080/get_time". Then, for the 

api_url = f"http://worldclockapi.com/api/json/{timezone}/now"

line, we create a variable called api_url to construct the URL for the WorldClock external API, and the {timezone} parameter is substituted with what the timezone variable contains (since we stored the client's timezone parameter, or lack thereof, into the timezone variable and because we added the "f" we make it an f string where we can substitute things within {} to their variable value). So requests.get() is used to send an HTTP GET request to WorldClock API, passing our completely constructed URL, and we then store the response of the request into the response variable. Once we have the response, we need to make sure it is status code 200 (success), and then we parse the JSON data and put it into the time_data variable via time_data = response.json(), and then retrieve the time_data's "currentDateTime" and store it into the current_time variable. If the status code is not 200, we handle the situation with the try/except block. If there is an error, it sets current_time to an appropriate error message. The last step here is to return the final response (whether it is an error message or the appropriate time) converted back into JSON to the client via

return jsonify({'time': current_time})

So, after navigating to the appropriate directory and running this file via python EndpointApp.py, it will let you know that it set up a local web server listening on port 8080 for GET requests at the /get_time endpoint. Then, after entering

"http://localhost:8080/get_time?timezone=est" 

into my web browser's URL, I was met with the following response:

{"time":"2023-10-23T14:22-04:00"}

Indicating that the code was a success.


			Client.py File

Next, for the Client.py file, the plan is to be able to run this Client.py file in the command prompt and then to receive the response from World Clock API into the command prompt, instead of having to manually type the URL: 

http://localhost:8080/get_time?timezone=est

into the web browser. 

So for this file, the first step is to perform the following required imports -- we import requests to handle HTTP requests, and sys so that we can accept parameters.

Then, the next step is to set the endpoint and store it in the endpoint_url variable by the following code:

endpoint_url = "http://localhost:8080/get_time"

After this step, in order to be able to make the complete GET request to the endpoint, we include the timezone parameter into the URL by the following code: 

params = {"timezone": timezone}

Here, we include whatever is in the timezone parameter, which has to be manually entered by the client when running the file:

python Client.py est

Where "est" is the timezone parameter.

Then, the syntax to make the GET request to the endpoint including the parameter and store the result of the request into the response variable is as follows:

response = requests.get(endpoint_url, params=params)

Once the response is in the response variable, we perform error handling logic in a try/except block by first checking if the status is a success (200) or a failure, we parse the JSON response via response.json, and we return the result back to the user.

Lastly, at the bottom, we have an if statement assessing whether or not the Client.py file is run by itself or if it is invoked by another program. If it is ran by itself, its contents include a user-friendly interaction that first assesses whether or not they entered a parameter along with the file, and whether or not that parameter is three characters. Remember, the correct syntax for running the file to find EST time is this:

python Client.py est

Once the correct syntax is entered, it will run the get_current_time method, passing sys.argv[1] parameter, and it will print the result back to the user.

			ClientCommandTest.py

This file is to test the Command Line Client, which is our Client.py file. More specifically, we are testing three scenarios - The first is a scenario where Client.py is run from the command prompt with a correct time zone parameter (which is the correct way to run the file --> python Client.py est), the second is where Client.py is run without a time zone parameter, and the third is where Client.py is run with an incorrect timezone parameter (esta instead of est).

First, we need to import unittest which allows us to test our code with test cases and suites. We also need to import subprocesses so we can generate scenarios or "subprocesses" that we need for testing, and so that we can connect to the output, input, and error pipes, and retrieve their return codes.

We then make a TestCommandLineClient class where we define three methods. The first is the method/scenario where the correct time zone parameter is entered. We create a subprocess with these characteristics, use subprocess.run to run this process, and store the result in the "result" variable. Stout=subprocess.PIPE captures the subprocesses' standard output, and stderr=subprocess.PIPE captures the standard error. I learned that Universal_newlines=True just makes it known to the system that our output needs to be decoded using our system's default text encoding. A positive return code for subprocesses is typically 0, which is why we have the line self.assertEqual(result.returncode, o). Lastly, for this method, we create a variable that stores the string "Current time in est", and then we check whether this string is present in the standard output of that method via "self.assertIn(expected_string, result.stdout)", which would indicate that the test was a success and the est parameter was viable since "Current time in est" was in fact returned.

Next, we have the method/scenario where no parameter is inputted, in which case we would still perform the steps listed in the previous method, but we would assert that the return code is "1" which is a failure, and we would assert that the error message we receive is equal to " 'Usage: python client.py <timezone>\n' ", which is what we typically would receive in the Client.py file in this scenario.

Then, we create the method/scenario where a parameter has 4 characters and is therefore incorrect -- again we would assert that the return code is "1" for a failure, and again and we would assert that the error message we receive is equal to " 'Usage: python client.py <timezone>\n' ".

When running this file to test the three test scenarios, the result in the command prompt should be as follows: 

"Ran 3 tests in 3.180s

OK"

			ClientMockTest.py File

This is to satisfy the following requirements: 
"Write unit tests using MOCKS that that test the endpoint – mock out the call to http://worldclockapi.com/api/json/est/now and just return a hard-coded value."

Just to summarize what this file accomplishes, test methods are set up in this file to validate the behavior of the get_current_time function from Client.py in two different scenarios: a successful request with a 200 status code and a failed request with a 404 status code. We make sure that the function behaves correctly in response to these different conditions and equals an expected response.

So in this file, we are testing the Client.py file and, importantly, we aren't making the actual call to the URL -- we are still calling the method, but instead we are giving our method the data it needs to engage the successful response code and also the data for a non-successful response code and seeing if it is equal to an expected outcome. 

To begin, we need to import unittest which allows us to both run and create tests. Then, when we import patch from unittest.mock, this is a decorator for temporarily replacing objects in a testable function with mock objects. The next step is to import requests, which we need in order to send HTTP requests in Python. Next, we need to import our Client.py method "get_current_time".

In our TestClient class, we patch the Client.py method "get_current_time" using @patch('requests.get') to mock the 'requests.get' function -- this means we patch the get function so we can control its characteristics. It is important to note that we aren't making an actual call with the Client.py file -- we are seeking to provide our own mock data. In our TestClient class we have the unittest.Testcase parameter which means that it inherits from unittest.Testcase. For our first method, the parameter "Self" is just an instance of the test class -- it is boilerplate code. The parameter "Mock_get" contains the mock data created by patch, and we pass it as a parameter so we can manipulate it within the method. For the following code:
mock_response = requests.Response() 
mock_response is an instance of requests.Response(), and we are sure to set the status code via mock_response.status_code = 200. For this case, 200 is a successful response. Next step is a bit trickier -- we need to create a mock JSON response -- we need to define a lambda function to simulate the JSON response -- in our special case, it returns a dictionary in brackets with a "time" field (key) containing a specific timestamp (value), and that line of code would look like this: 

mock_response.json = lambda: {"time": "2023-10-27T15:30:00Z"}

Then, we need this code:

mock_get.return_value = mock_response

To ensure that when requests.get is called during the test, it will return the mock_response object which has our specific data.

Next, we call the 'get_current_time' function and we pass the eastern standard time (est) parameter, invoking the behavior of the method in the Client.py file with the est parameter and the mock data, and storing the result in the result variable. Then, we assert that the expected response equals what our Client.py method provides when the Client.py method is given our mock data.

The next method in the ClientMockTest.py file is test_failed_request, and is very similar to the method above. Instead, we make the status code an error code, which is anything that is not 200, and in this case we make it 404. We then mock the JSON response to the corresponding error message:

mock_response.json = lambda: {"error": "Time not available"}

and we need to confirm if passing these unsuccessful parameters signals for the Client.py file to return " 'Failed to fetch time from the endpoint. Status code: 404' " -- We again made a variable that holds this same string, and used the assertEqual method to confirm this.

Lastly, this code here:
"if __name__ == '__main':
    unittest.main()
"
is used to ensure that the test methods only run when it is directly run and not imported as a module somewhere else - so, when it is run directly, unittest.main() runs the two test methods.

After running this code in the command prompt, given that the World Clock API is up and running, the result should be as follows:

Ran 2 tests in 0.001s

OK


			ClientLiveEndpointTest.py

This file is to satisfy the following requirement: "Write an Acceptance test that tests the live endpoint. (http://worldclockapi.com/api/json/est/now is actually called)"

To begin, we need to import unittest which allows us to both run and create tests, and we also need to import subprocess so we can run a subprocess from Client.py The first method we create is test_live_successful_client_request() where the goal is to run a process where the Client.py file is ran with a proper est parameter, and assess whether or not the exact time received equals what we have in our expected output variable. This differs from the ClientCommandTest.py file because in that file, we are assessing simply whether or not the expected output contains "Current time in est", whereas in this file we are assessing whether or not the exact output is a match. For this reason, we need to ensure we update line 23 to our current time, which by default is this: 

expected_output = "Current time in est: 2023-11-11T10:53-05:00\n"
