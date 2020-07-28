class ApiRequestError(Exception):
    def __init__(self, request_url: str, error_message: str, status_code: int):
        self.url = request_url
        self.message = error_message
        self.status_code = status_code

    def __str__(self):
        return f"Error getting {self.url} with {self.status_code} status code: {self.message}"
