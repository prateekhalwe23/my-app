from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/healthz':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "healthy", "version": "1.0.0"}).encode())
        else:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Hello from my-app!", "version": "1.0.0"}).encode())

if __name__ == '__main__':
    print("Starting server on port 8080...")
    HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
