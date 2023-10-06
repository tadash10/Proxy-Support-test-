import time

class ProxyRotation:
    def __init__(self, multi_proxy_support, rotation_interval):
        self.multi_proxy_support = multi_proxy_support
        self.rotation_interval = rotation_interval

    def start_rotation(self):
        while True:
            time.sleep(self.rotation_interval)
            next_proxy = self.multi_proxy_support.use_next_proxy()
            if next_proxy:
                print(f"Rotated to the next proxy: {next_proxy}")
