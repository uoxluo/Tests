#!/usr/bin/env python

import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
import time
import asyncio
import websockets


class HTTPThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        # Start the HTTP server on port 80
        httpd = HTTPServer(("", 80), SimpleHTTPRequestHandler)

        # https
        #import ssl
        #httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="key.pem", certfile="cert.pem", server_side=True)

        httpd.serve_forever()

http_thread = HTTPThread()
http_thread.daemon = True
http_thread.start()

i = 0
async def data_sender(ws, path):
    global i
    while True:
        await ws.send(str(i))
        i = i + 1
        time.sleep(0.1)

ws_server = websockets.serve(data_sender, "", 81)
asyncio.get_event_loop().run_until_complete(ws_server)
asyncio.get_event_loop().run_forever()