import logging

class LoggingAndReporting:
    def __init__(self, log_file):
        logging.basicConfig(filename=log_file, level=logging.INFO)

    def log_request(self, url, status_code, response_time):
        # Log details of a request, including URL, status code, and response time
        logging.info(f"Request to {url} | Status Code: {status_code} | Response Time: {response_time} seconds")
