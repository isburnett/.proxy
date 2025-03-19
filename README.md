# Full-Functional Proxy Server

This is a fully-functional HTTP/HTTPS proxy server built in Python. It includes support for caching, rate limiting, logging, and SSL encryption.

## Features
- **HTTP/HTTPS Proxying**: Handles both HTTP and HTTPS requests.
- **Caching**: Caches GET responses for faster access on subsequent requests.
- **Rate Limiting**: Limits the number of requests per minute from a single IP.
- **Logging**: Logs detailed information about every request and response.
- **Error Handling**: Detailed error responses for timeouts and bad requests.

## Requirements
- Python 3.x
- `requests` module (`pip install -r requirements.txt`)

## Setup

1. Generate SSL certificates (`server.crt` and `server.key`).
2. Update configuration in `config.py` as needed.
3. Run the proxy server using `python server.py`.

## Example Usage

Run the proxy server on `https://localhost:8443`. To access the proxy:
