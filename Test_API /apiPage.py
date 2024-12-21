import requests

class apiPage:

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url


    def post_list(self, url: str,ss):
         resp = requests.post(self.base_url+url, headers=ss)
         return resp


    def post_product(self, url, data, ss):
        resp = requests.post(self.base_url+url, data=data, headers=ss)
        return resp

