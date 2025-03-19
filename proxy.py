# proxy.py
import requests
from urllib.parse import urlparse
from http.server import SimpleHTTPRequestHandler
from utils import log_request, check_rate_limit
from config import CORS_ALLOWED_ORIGINS
from cache import get_from_cache, add_to_cache

class ProxyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def _set_cors_headers(self):
        """Set CORS headers for allowing cross-origin requests."""
        self.send_header('Access-Control-Allow-Origin', ', '.join(CORS_ALLOWED_ORIGINS))
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')

    def do_OPTIONS(self):
        """Handle OPTIONS request for CORS preflight."""
        self.send_response(200)
        self._set_cors_headers()
        self.end_headers()

    def do_GET(self):
        url = self.path[1:]  # Remove the leading '/'
        ip = self.client_address[0]

        # Check rate limiting
        if not check_rate_limit(ip):
            self.send_response(429)  # Too many requests
            self.end_headers()
            self.wfile.write(b"Rate limit exceeded")
            return
        
        # Check cache first
        cached_response = get_from_cache(url)
        if cached_response:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self._set_cors_headers()
            self.end_headers()
            self.wfile.write(cached_response)
            log_request("GET", url, 200, ip)
            return
        
        try:
            response = requests.get(url)
            self.send_response(response.status_code)
            self.send_header("Content-type", response.headers["Content-Type"])
            self._set_cors_headers()
            self.end_headers()
            self.wfile.write(response.content)  # Send the response back to the client

            # Cache the response
            add_to_cache(url, response.content)
            log_request("GET", url, response.status_code, ip)
        except requests.exceptions.RequestException as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Error forwarding GET request")
            log_request("GET", url, 500, ip)

    def do_POST(self):
        url = self.path[1:]  # Remove the leading '/'
        ip = self.client_address[0]

        # Check rate limiting
        if not check_rate_limit(ip):
            self.send_response(429)  # Too many requests
            self.end_headers()
            self.wfile.write(b"Rate limit exceeded")
            return
        
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            response = requests.post(url, data=post_data, headers=dict(self.headers))
            self.send_response(response.status_code)
            self.send_header("Content-type", response.headers["Content-Type"])
            self._set_cors_headers()
            self.end_headers()
            self.wfile.write(response.content)  # Send the response back to the client
            log_request("POST", url, response.status_code, ip)
        except requests.exceptions.RequestException as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Error forwarding POST request")
            log_request("POST", url, 500, ip)
