#!/usr/bin/python3
"""Module that add a class who deal with the requests of web site, and a script
that start a local http server"""
import http.server
import json


class dynamic_handler(http.server.BaseHTTPRequestHandler):
    """Class that deal with the requests of the users"""

    def do_GET(self):
        """All the methods to deal with some endpoints"""
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            new_dict = {"name": "John", "age": 30, "city": "New York"}
            data = json.dumps(new_dict)
            self.wfile.write(data.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode("UTF-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            new_dict = {"version": "1.0",
                        "description": "A simple API built with http.server"}
            data = json.dumps(new_dict)
            self.wfile.write(data.encode("utf-8"))

        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            response = "Hello, this is a simple API!"
            self.wfile.write(response.encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))


server_adress = ('localhost', 8000)
instance_server = http.server.HTTPServer(server_adress, dynamic_handler)
print("serveur en cours d'execution")
instance_server.serve_forever()
