import random

class ProxyPooling:
    def __init__(self, proxy_list):
        self.proxy_list = proxy_list

    def get_random_proxy(self):
        # Select a random proxy from the pool
        return random.choice(self.proxy_list)

    def distribute_requests(self, num_requests):
        # Distribute requests across the proxy pool
        proxies = [self.get_random_proxy() for _ in range(num_requests)]
        return proxies
