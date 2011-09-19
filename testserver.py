from os import chdir
from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import HTTPServer

chdir("timetracker")
server = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
server.serve_forever()
