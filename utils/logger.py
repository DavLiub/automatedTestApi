import datetime
import os
from requests import Response

date = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

class Logger():
    logs_directory = "logs"
    file_name = os.path.join(logs_directory, f"log_{date}.log")

    @classmethod
    def write_log_to_file(cls, data: str):
        """Write the provided data to the log file."""
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)
            print(os.path.abspath(logger_file.name))

    @classmethod
    def add_request(cls, url: str, method: str, body=None):
        """Add a log entry for a request."""
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        data_to_add = f"\nTest: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += f"Request body: {body}\n"
        data_to_add += "\n"
        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, result: Response):
        """Add a log entry for a response."""
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)
        data_to_add = f"Response code: {result.status_code}\n"
        data_to_add += f"Response text: {result.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n\n"
        cls.write_log_to_file(data_to_add)

