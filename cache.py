# cache.py
import time
from config import CACHE_ENABLED, CACHE_TIMEOUT

cache_store = {}

# Cache lookup and store functions
def get_from_cache(url):
    if CACHE_ENABLED and url in cache_store:
        cached_response = cache_store[url]
        if time.time() - cached_response['timestamp'] < CACHE_TIMEOUT:
            return cached_response['response']
    return None

def add_to_cache(url, response):
    if CACHE_ENABLED:
        cache_store[url] = {
            'response': response,
            'timestamp': time.time()
        }
