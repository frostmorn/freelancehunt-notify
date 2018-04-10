import base64
import hmac
import hashlib
import requests

class Freelancehunt(object):
#   TODO: Message delivering
    # fields:
    api_token = None
    api_secret = None

    def __init__(self, api_token, api_secret):
        self.api_token = api_token
        self.api_secret = api_secret

    def __sign(self, url, method, post_params):
        return base64.standard_b64encode(
            hmac.new(key=self.api_secret.encode('utf-8'),
                    msg=(url+method+post_params).encode('utf-8'),
                    digestmod=hashlib.sha256).digest()).decode('utf-8')

    def __request(self, url, post_params=''):
        method = 'GET'
        signature = self.__sign(url, method, post_params)
        r = requests.get(url, auth=(self.api_token, signature))
        return r.text

    def get_feed(self, post_params=''):
        url = 'https://api.freelancehunt.com/my/feed'
        return self.__request(url, post_params)