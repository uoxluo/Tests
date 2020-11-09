#!/usr/bin/env python

from http.server import HTTPServer, CGIHTTPRequestHandler
import ssl

# Start the CGIHTTP server on port 443
httpd = HTTPServer(("", 443), CGIHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="key.pem", certfile="cert.pem", server_side=True)
httpd.serve_forever()
