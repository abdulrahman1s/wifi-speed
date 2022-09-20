from ..util import *
from pyquery import PyQuery as pq


class BaseRouter:
    def __init__(self):
        self.url = "https://192.168.1.1"
        self.speeds = []
        self.fetch = fetch_client()
        self.html = pq(self.fetch.get(self.url).text)
        self.logged_in = False

    def login(self, username, password):
        raise "Not Implemented"

    def set_speed(self, speed):
        raise "Not Implemented"

class RouterException(Exception):
    def __init__(self, message) -> None:
        super().__init__()
        self.message = message
