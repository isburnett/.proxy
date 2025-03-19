# config.py
# Configuration for the proxy server.

HOST = 'localhost'  # Proxy server host
PORT = 8443  # Port for HTTPS
CERTIFICATE_PATH = 'server.crt'  # SSL Certificate file path
KEY_PATH = 'server.key'  # SSL Key file path

# CORS Settings
CORS_ALLOWED_ORIGINS = ["*"]  # Allows all origins or specific URLs, e.g., ["https://your-website.com"]

# Caching and Rate Limiting
CACHE_ENABLED = True
CACHE_TIMEOUT = 60  # Cache timeout in seconds
RATE_LIMIT_ENABLED = True
MAX_REQUESTS_PER_MINUTE = 60  # Max requests per minute from a single IP
