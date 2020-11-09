#!/usr/bin/env python

from http.server import HTTPServer, SimpleHTTPRequestHandler

# Start the HTTP server on port 80
httpd = HTTPServer(("", 80), SimpleHTTPRequestHandler)
# https
#import ssl
#httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="key.pem", certfile="cert.pem", server_side=True)
httpd.serve_forever()