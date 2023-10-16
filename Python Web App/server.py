#!/usr/bin/python

# Jack Cacela and Spencer Marks
# This Python Web App accepts a Celsius value and returns the value in Fahrenheit.

# You need the index.html file in the same folder so it can be referenced from this file.
# If you want to use the command prompt, navigate to the appropriate directory and, after running the server.py file, go to your favorite web browser and type localhost:8080 into the search bar.



# These three are for HTTP server functionality, making a socket server, and for handling URLs and query strings, respectively.
import http.server
import socketserver
from urllib.parse import urlparse, parse_qs

# This sets the port number where the web server listens for requests.
PORT = 8080

# This class below lets us handle HTTP requests and responses.
class MyHandler(http.server.SimpleHTTPRequestHandler):
# Below, the standard GET method from the standard SimpleHTTPRequestHandler class is overridden with the "do_GET method" which is called when HTTP Get request is received
    def do_GET(self):
# Now we need to use the urlparse function to get path and query parameters.
        parsed_url = urlparse(self.path)
# If the path is /convert, this means the request to turn Celsius to Fahrenheit is being made due to the path attribute in the index.html file.
        if parsed_url.path == "/convert":
# If the path is /convert, will now use parse_qs to extract query params including Celsius value, and store them in the query variable.
            query = parse_qs(parsed_url.query)
# Now we will extract the "celsius" parameter from the query parameters. If it doesn't exist, our default will be to an empty string "".
            celsius = query.get("celsius", [""])[0]
# The next step is to call our convert to fahrenheit method (defined below) and send the status code 200 which means the request is successful.
            fahrenheit = self.convert_to_fahrenheit(celsius)
            self.send_response(200)
# This code below then sets the response content to text / html with UTF-8 encoding to ensure the response is in proper format.
            self.send_header("Content-type", "text/html; charset=utf-8")  
# "End_headers" signals the end of the HTTP response headers.
            self.end_headers()
# Self.wfile.write ensures that Fahrenheit is converted to UTF-8 when writing the value to the response.
            self.wfile.write(fahrenheit.encode("utf-8")) 
# Now, if the path is not /convert, (no value has been entered and the convert button has not been clicked on) we will just return the standard, static page: 
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")  
            self.end_headers()
# Open the HTML file with UTF-8 encoding
            with open("index.html", "r", encoding="utf-8") as file:  
                content = file.read()
                self.wfile.write(content.encode("utf-8"))  

    def convert_to_fahrenheit(self, celsius):
        try:
# Tries to convert the inputted string celsius value to a float integer 
            celsius = float(celsius)
            fahrenheit = (celsius * 9/5) + 32
# Now we will return an f string, which means that Python evaluates the expressions inside the curly braces {} and inserts their values into the string. So, if celsius is 20.0 and fahrenheit is 68.0, the resulting string will be "20.0°C is 68.0°F."
            return f"{celsius}°C is {fahrenheit}°F"
        except ValueError:
            return "Invalid input. Please enter a valid number."
# Create a TCP server using the socketserver.TCPServer class, specifying the address ("", which just means it will listen on all available network interfaces) and the port (PORT).
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
#Now we will just print this message below confirming the server is running and listening on the port.
    print("serving at port", PORT)
#This starts the server and it will serve requests forever.
    httpd.serve_forever()
