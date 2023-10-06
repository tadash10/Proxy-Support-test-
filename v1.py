import requests

class ProxyClient:
    def __init__(self):
        self.session = requests.Session()
        self.proxies = {}

    def set_proxy(self, proxy_type, proxy_url, username=None, password=None):
        """
        Set up proxy settings for the client.

        Args:
            proxy_type (str): The type of proxy, e.g., 'http', 'https', 'socks5'.
            proxy_url (str): The URL of the proxy server (e.g., 'http://proxyserver.com:8080').
            username (str, optional): Username for proxy authentication.
            password (str, optional): Password for proxy authentication.

        Returns:
            bool: True if proxy settings were successfully applied, False otherwise.
        """
        try:
            if username and password:
                self.proxies[proxy_type] = f"{proxy_type}://{username}:{password}@{proxy_url}"
            else:
                self.proxies[proxy_type] = f"{proxy_type}://{proxy_url}"
            return True
        except Exception as e:
            print(f"Failed to set up proxy: {e}")
            return False

    def send_request(self, method, url, **kwargs):
        """
        Send an HTTP request through the configured proxy.

        Args:
            method (str): HTTP method (e.g., 'GET', 'POST', 'PUT', 'DELETE').
            url (str): The URL of the target resource.
            kwargs (dict): Additional parameters to pass to the requests library.

        Returns:
            requests.Response: The response object from the HTTP request.
        """
        try:
            response = self.session.request(method, url, proxies=self.proxies, **kwargs)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

if __name__ == "__main__":
    proxy_client = ProxyClient()
    
    # Example proxy setup
    proxy_type = 'http'
    proxy_url = 'http://proxyserver.com:8080'
    username = 'your_username'
    password = 'your_password'
    
    if proxy_client.set_proxy(proxy_type, proxy_url, username, password):
        target_url = 'https://example.com'
        response = proxy_client.send_request('GET', target_url)
        
        if response:
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.text}")
        else:
            print("Request failed.")
