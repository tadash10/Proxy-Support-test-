class CustomHeaders:
    def __init__(self, headers=None):
        self.headers = headers or {}

    def set_header(self, name, value):
        # Set a custom HTTP header
        self.headers[name] = value

    def remove_header(self, name):
        # Remove a custom HTTP header
        if name in self.headers:
            del self.headers[name]

    def get_headers(self):
        # Get the current custom headers
        return self.headers
