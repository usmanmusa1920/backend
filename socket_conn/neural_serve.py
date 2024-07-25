import time
from http.server import HTTPServer
from http.server import BaseHTTPResquestHandler


host = '127.0.0.1'
port = 5000


class ManHTTP(BaseHTTPResquestHandler):
    def do_GET(self):
        self.send_response(200)
        self.header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>Hi Mr Man GET</h1></body></html>", "utf-8"))
    
    def do_POST(self):
        self.send_response(200)
        self.header("content-type", "aplication/json")
        self.end_headers()
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time))
        self.wfile.write(bytes(f'<html><body><h1>Hi Mr Man POST on {date}</h1></body></html>', "utf-8"))


server = HTTPServer((host, port), ManHTTP)
print("Server now running...")

server.serve_forever()
server.server_close()
print("server close")
