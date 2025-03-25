import requests
import yaml
import os

class APIRequest:
    def __init__(self):
        # get config file
        config_path = os.path.join(os.path.dirname(__file__), "../config/config.yaml")
        with open(config_path, "r", encoding="utf-8") as file:
            self.config = yaml.safe_load(file)
        self.base_url = self.config["base_url"]
        self.headers = self.config["headers"]

    def send_request(self, method, endpoint, data=None, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        headers = headers or self.headers

        response = requests.request(method, url, json=data, params=params, headers=headers)
        return response
