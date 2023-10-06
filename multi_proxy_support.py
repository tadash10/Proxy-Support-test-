class MultiProxySupport:
    def __init__(self):
        self.proxies = []

    def add_proxy(self, proxy):
        # Add a new proxy configuration to the list
        self.proxies.append(proxy)

    def remove_proxy(self, proxy):
        # Remove a proxy configuration from the list
        if proxy in self.proxies:
            self.proxies.remove(proxy)

    def use_next_proxy(self):
        # Rotate to the next proxy in the list
        if self.proxies:
            next_proxy = self.proxies.pop(0)
            self.proxies.append(next_proxy)
            return next_proxy

    def get_active_proxies(self):
        # Get the list of currently active proxies
        return self.proxies
