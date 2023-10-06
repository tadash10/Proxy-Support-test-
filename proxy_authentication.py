class ProxyAuthentication:
    def __init__(self):
        self.credentials = {}

    def add_credentials(self, proxy, username, password):
        # Store proxy-specific authentication credentials securely
        self.credentials[proxy] = (username, password)

    def get_credentials(self, proxy):
        # Retrieve credentials for a specific proxy
        return self.credentials.get(proxy, None)
