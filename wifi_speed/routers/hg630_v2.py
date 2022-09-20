from .base import BaseRouter, RouterException
from ..util import *
from base64 import b64encode
from hashlib import sha256
import json

class HG630_v2(BaseRouter):
    def __init__(self):
        super().__init__()

        self.speeds = [
            "1", "2", "5.5", "6", "9", "11",
            "12", "18", "24", "36", "48", "54", "default"
        ]
        self.speed = self.speeds[-1]
        self.power = 100
        self.csrf = {
            "csrf_token": "",
            "csrf_param": ""
        }

        for meta in self.html.items("meta"):
            if meta.attr("name") == "csrf_param":
                self.csrf["csrf_param"] = meta.attr("content")
            if meta.attr("name") == "csrf_token":
                self.csrf["csrf_token"] = meta.attr("content")

    def login(self, username, password):
        pwd = username
        pwd += b64encode(sha256(password.encode("utf-8")
                                ).hexdigest().encode("utf-8")).decode("utf-8")
        pwd += self.csrf["csrf_param"]
        pwd += self.csrf["csrf_token"]
        pwd = sha256(pwd.encode("utf-8")).hexdigest()
        payload = {
            "csrf": self.csrf,
            "data": {
                "UserName": username,
                "Password": pwd
            }
        }

        page = self.fetch.post(f"{self.url}/api/system/user_login", data=json.dumps(payload))

        if '"errorCategory":"ok"' in page.text:
            data = json.loads(page.text[12:-2])
            self.csrf["csrf_param"] = data["csrf_param"]
            self.csrf["csrf_token"] = data["csrf_token"]
            self.logged_in = True
        else:
            raise RouterException("Invalid username or password")

    def set_speed(self, speed):
        if not self.logged_in:
            raise Exception("Missing credentials")

        if speed not in self.speeds:
            raise Exception("Invalid speed value")

        payload = {
            "csrf": self.csrf,
            "action": "SendSettings",
            "data": {
                "config2g": {
                    "ID": "InternetGatewayDevice.LANDevice.1.WLANConfiguration.1.",
                    "country": "EG",
                    "power": self.power,
                    "mode": "b/g",
                    "channel": 0,
                    "wmm": True,
                    "rate": "0" if speed == "default" else speed
                }
            }
        }

        try:
            self.fetch.post(f"{self.url}/api/ntwk/WlanBasic?showpass=false", data=json.dumps(payload), timeout=1)
        except Exception as err:
            if not "HTTPSConnectionPool" in str(err):
                raise err
