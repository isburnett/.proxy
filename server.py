# server.py
import http.server
import ssl
from proxy import ProxyHTTPRequestHandler
from config import HOST, PORT, CERTIFICATE_PATH, KEY_PATH
from utils import setup_logging

def run():
    setup_logging()  # Initialize logging
    server_address = (HOST, PORT)
    httpd = http.server.HTTPServer(server_address, ProxyHTTPRequestHandler)
    
    # Wrap the server with SSL for HTTPS support
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   keyfile=KEY_PATH,
                                   certfile=CERTIFICATE_PATH,
                                   server_side=True)

    print(f"Proxy server running on https://{HOST}:{PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
