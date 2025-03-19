# utils.py
import logging
import time
from config import RATE_LIMIT_ENABLED, MAX_REQUESTS_PER_MINUTE
from collections import defaultdict

# Set up logging
def setup_logging():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    logging.info("Logging is enabled.")

# Rate Limiting: Track request count per IP
request_tracker = defaultdict(list)

def check_rate_limit(ip):
    if RATE_LIMIT_ENABLED:
        current_time = time.time()
        # Filter out requests older than a minute
        request_tracker[ip] = [timestamp for timestamp in request_tracker[ip] if current_time - timestamp < 60]

        if len(request_tracker[ip]) >= MAX_REQUESTS_PER_MINUTE:
            return False  # Rate limit exceeded
        else:
            request_tracker[ip].append(current_time)
            return True
    return True

# Function to log request information
def log_request(method, url, status_code, ip):
    logging.info(f"Request {method} to {url} from IP {ip} - Status Code: {status_code}")
